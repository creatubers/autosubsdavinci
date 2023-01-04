import DaVinciResolveScript as dvr_script
import sys
import time
from os.path import join, expanduser
from os import system, remove

resolve = dvr_script.scriptapp("Resolve")


def add_timeline_to_render(project, timeline, presetName, targetDirectory, renderFormat, renderCodec):
    project.SetCurrentTimeline(timeline)
    project.LoadRenderPreset(presetName)

    if not project.SetCurrentRenderFormatAndCodec(renderFormat, renderCodec):
        return False

    project.SetRenderSettings(
        {"SelectAllFrames": 1, "TargetDir": targetDirectory, "ExportVideo": False, "ExportAudio": True,
         "CustomName": timeline_name_vosk})
    return project.AddRenderJob()


def render_all_timelines(resolve, timeline, presetName, targetDirectory, renderFormat, renderCodec):
    project_manager = resolve.GetProjectManager()
    project = project_manager.GetCurrentProject()
    if not project:
        return False

    resolve.OpenPage("Deliver")

    if not add_timeline_to_render(project, timeline, presetName, targetDirectory, renderFormat, renderCodec):
        return False
    return project.StartRendering()


def is_rendering_in_progress(resolve):
    project_manager = resolve.GetProjectManager()
    project = project_manager.GetCurrentProject()
    if not project:
        return False

    return project.is_rendering_in_progress()


def wait_for_rendering_completion(resolve):
    while is_rendering_in_progress(resolve):
        time.sleep(1)
    return


def delete_all_render_jobs(resolve):
    project_manager = resolve.GetProjectManager()
    project = project_manager.GetCurrentProject()
    project.delete_all_render_jobs()
    return


renderPresetName = "H.264 Master"
renderPath = expanduser('~')
renderFormat = "mp4"
renderCodec = "H264"

# Get currently open project

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
project.delete_all_render_jobs()
timeline = project.GetCurrentTimeline()
timeline_name = timeline.GetName()
timeline_name = timeline_name.replace(" ", "")
timeline_name_vosk = timeline_name + 'subvosk'

if not render_all_timelines(resolve, timeline, renderPresetName, renderPath, renderFormat, renderCodec):
    print("Unable to set all timelines for rendering")
    sys.exit()

wait_for_rendering_completion(resolve)

delete_all_render_jobs(resolve)

print("Rendering is completed.")
video = join(renderPath, timeline_name_vosk + ".mp4")
subtitle = join(renderPath, timeline_name + ".srt")
s = f"vosk-transcriber -l es -i {video} -t srt -o {subtitle}"

system(s)

resolve.OpenPage("Edit")
media_pool = project.GetMediaPool()

media_pool.ImportMedia(subtitle)
remove(video)
