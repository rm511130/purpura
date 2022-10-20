import bpy
from pathlib import Path


while bpy.data.objects:
  bpy.data.objects.remove(bpy.data.objects[0], do_unlink=True)

bpy.ops.wm.usd_import(filepath="C:\\Users\\Ralph\\3D Objects\\Running Girl Animation\\spring.runcycle.usd", relative_path=True, read_mesh_colors=True,import_usd_preview=True)

context = bpy.context
scene = context.scene
viewlayer = context.view_layer

bpy.ops.object.select_by_type(extend=False, type='MESH') 
bpy.ops.export_mesh.stl(
        filepath="C:\\Users\\Ralph\\3D Objects\\Running Girl Animation\\RunningGirl.STL", use_selection=True, 
        global_scale=1.0, use_scene_unit=False, ascii=False, use_mesh_modifiers=True, 
        batch_mode="OFF", axis_forward="Y", axis_up="Z")

bpy.ops.export_scene.gltf(
        filepath="C:\\Users\\Ralph\\3D Objects\\Running Girl Animation\\RunningGirl.GLB",
        check_existing=False, export_format="GLB", ui_tab="GENERAL")

obs = [o for o in scene.objects if o.type == 'MESH']
bpy.ops.object.select_all(action='DESELECT')    

path = Path("C:\\Users\\Ralph\\3D Objects\\Running Girl Animation")
for ob in obs:
    viewlayer.objects.active = ob
    ob.select_set(True)
    stl_path = path / f"{ob.name}.stl"
    bpy.ops.export_mesh.stl(
            filepath=str(stl_path),
            use_selection=True)
    glb_path = path / f"{ob.name}.glb"        
    bpy.ops.export_scene.gltf(
            filepath=str(glb_path),
            check_existing=False, export_format="GLB", ui_tab="GENERAL",
            use_selection=True)
    ob.select_set(False)