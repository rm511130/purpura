## 20 OCT 2022
## Proof of Concept Code by rmeira@physna.com
## usd2glb
##
## Combined purpose:
##   1. Convert a single USD file into GLB
##   2. Convert all subcomponents of USD file into GLBs
##
## Requires: Blender 3.3 or later
## Code is to be executed as headless / background service
## 
#########################
## PowerShell Example: ##
#########################
##
## C:> cd "C:\Program Files\Blender Foundation\Blender 3.3"
## C:\Program Files\Blender Foundation\Blender 3.3> .\blender.exe -b -P "C:\Users\Ralph\Python\usd2glb.py" -- -i "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\HumanFemale.usd" -o "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\output" -s "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\HumanFemale.glb"
## 
## Where:
##        -b = background or headless
##        -P = Python
##        Python code = "C:\Users\Ralph\Python\usd2glb.py" 
##        -- = subsequent parameters are inputs for the Python code
##        -i = input USD file name and location
##        Example of USD file name and location = "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\HumanFemale.usd" 
##        -o = output directory where all USD subcomponents will be saved as GLB files
##        Example of output directory: "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\output" 
##        -s = file name and location of single GLB file conversion from USD file
##        Example of Single GLB file name and location: "C:\\Users\\Ralph\\3D Objects\\Human Pixar Woman\\HumanFemale.glb"
##
## Notes:
##        - Directories referred to in "-i", "-o" and "-s" must already exist
##        - Note the need for double backslashes when passing parameters to the Python code
## 
## The output on the PowerShell Console will look something like this:
##
##        Blender 3.3.1 (hash b292cfe5a936 built 2022-10-05 00:49:25)
##        Read prefs: C:\Users\Ralph\AppData\Roaming\Blender Foundation\Blender\3.3\config\userpref.blend
##        USD import of 'C:\Users\Ralph\3D Objects\Human Pixar Woman\HumanFemale.usd' took 53.7 ms
##        Blender quit

import argparse
import bpy
from pathlib import Path

def get_args():
  parser = argparse.ArgumentParser()
  _, all_arguments = parser.parse_known_args()
  double_dash_index = all_arguments.index('--')
  script_args = all_arguments[double_dash_index + 1: ]
  parser.add_argument('-i', '--input', help="Path and filename of USD file")
  parser.add_argument('-o', '--output', help="Path of existing directory where GLBs will be placed")
  parser.add_argument('-s', '--single', help="Path and filename of single file USD to GLB conversion")
  parsed_script_args, _ = parser.parse_known_args(script_args)
  return parsed_script_args

args = get_args()

while bpy.data.objects:
  bpy.data.objects.remove(bpy.data.objects[0], do_unlink=True)

bpy.ops.wm.usd_import(filepath=args.input, relative_path=True, read_mesh_colors=True,import_usd_preview=True)

context = bpy.context
scene = context.scene
viewlayer = context.view_layer

bpy.ops.object.select_by_type(extend=False, type='MESH') 
bpy.ops.export_scene.gltf(
        filepath=args.single,
        check_existing=False, export_format="GLB", ui_tab="GENERAL")
  
obs = [o for o in scene.objects if o.type == 'MESH']
bpy.ops.object.select_all(action='DESELECT')    

path = Path(args.output)
for ob in obs:
    viewlayer.objects.active = ob
    ob.select_set(True)
    glb_path = path / f"{ob.name}.glb"
    bpy.ops.export_scene.gltf(
            filepath=str(glb_path),
            check_existing=False, export_format="GLB", ui_tab="GENERAL",
            use_selection=True)
    ob.select_set(False)
