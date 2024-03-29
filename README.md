# autosubsdavinci
Script para pasar voz a texto en líneas de tiempo de DaVinci Resolve usando VOSK.

Para su correcto funcionamiento solo tienes que seguir estos pasos:

1) Instala FFmpeg. La manera más fácil de hacerlo en Windows es mediante Chocolatey: 
<code>choco install ffmpeg -y</code>
2) Instala DaVinci Resolve 18+ en su versión Studio y activa la programación mediante scripts: abrimos el programa, nos vamos a Preferencias y, en la pestaña Sistema, nos vamos al apartado General. Aquí, en "Programación externa mediante" seleccionamos Local. Luego, cierra el programa
3) Instala Python 3 desde su web oficial: https://www.python.org/downloads/ y asegurándote de que tienes activada la opción de instalar PIP y las variables de entorno de Python. En Windows, es mejor instalar Python en el directorio raíz de tu disco duro principal. Por ejemplo, C:\Python3\
4) Instala las variables de entorno de DaVinci Resolve (extraído de la documentación oficial de DaVinci Resolve):

Mac OS X:
    RESOLVE_SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
    RESOLVE_SCRIPT_LIB="/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
    PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"

Windows:
    RESOLVE_SCRIPT_API="%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting"
    RESOLVE_SCRIPT_LIB="C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll"
    PYTHONPATH="%PYTHONPATH%;C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules"

Linux:
    RESOLVE_SCRIPT_API="/opt/resolve/Developer/Scripting"
    RESOLVE_SCRIPT_LIB="/opt/resolve/libs/Fusion/fusionscript.so"
    PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"
    
5) Instala VOSK (https://alphacephei.com/vosk/) mediante 

<code>pip3 install vosk</code>

En Windows, además, tienes que añadir en C:\Usuarios\nombredeusuario\ un directorio llamado .cache y, dentro de este, otro llamado vosk

6) Instala el script de este repositorio en la carpeta Utility de DaVinci Resolve
