# Purpura
Blender Python Script for converting a USD file into STL format

## 14 OCT 2022 - Proof of Concept Code by rmeira@physna.com
- Property of Physna
- Purpura Project

## Combined purposes:
   1. Convert single USD file into STL
   2. Convert all subcomponents of USD file into STLs

## Requires: 
   - Blender 3.3 or later
   - Code is to be executed as headless / background service
 
## How to execute:

### PowerShell Example:

```
C:> cd "C:\Program Files\Blender Foundation\Blender 3.3"
C:\Program Files\Blender Foundation\Blender 3.3> .\blender.exe -b -P "C:\Users\Ralph\3D Objects\Kitchen\Purpura-Executable\purpura-03.py" -- -i "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\HumanFemale.usd" -o "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\output" -s "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\HumanFemale.stl"
```
### Where:
```
-b = background or headless

-P = Python

Python Script = "C:\Users\Ralph\3D Objects\Kitchen\Purpura-Executable\purpura-03.py" 

-- = subsequent parameters are inputs for the Python code

-i = input USD file name and location
     Example of USD file name and location = "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\HumanFemale.usd" 

-o = output directory where all USD subcomponents will be saved as STL files
     Example of output directory: "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\output" 

-s = file name and location of single STL file conversion from USD file
     Example of Single STL file name and location: "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\HumanFemale.stl"
```

### Notes:
       - Directories referred to in "-i", "-o" and "-s" must already exist
       - Note the need for double backslashes when passing parameters to the Python code
 
## The output on the PowerShell Console will look something like this:

```       
Blender 3.3.1 (hash b292cfe5a936 built 2022-10-05 00:49:25)
Read prefs: C:\Users\Ralph\AppData\Roaming\Blender Foundation\Blender\3.3\config\userpref.blend
USD import of 'C:\Users\Ralph\3D Objects\Human Pixar Woman\HumanFemale.usd' took 53.7 ms
Blender quit
```

# Step-by-Step 

1. Download examples of USD files from: https://graphics.pixar.com/usd/release/dl_downloads.html#assets

