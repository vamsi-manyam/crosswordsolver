### SET FOLDER TO WATCH + FILES TO WATCH + SUBFOLDERS YES/NO
    $watcher = New-Object System.IO.FileSystemWatcher
    $watcher.Path = Join-Path $PSScriptRoot "\watch"
    $watcher.Filter = "*.png"
    $watcher.IncludeSubdirectories = $false
    $watcher.EnableRaisingEvents = $false

### DEFINE ACTIONS AFTER AN EVENT IS DETECTED
    $action = { $path = $Event.SourceEventArgs.FullPath
                cmd.exe /C python python\run.py $path
              }    
### DECIDE WHICH EVENTS SHOULD BE WATCHED 
    Register-ObjectEvent $watcher "Changed" -Action $action
    while ($true) {sleep 1}