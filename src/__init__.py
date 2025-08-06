bl_info = {
    "name": "Reset Workspace",
    "description": "Reset the user interface (with your startup file interface)",
    "author": "Lukas Sabaliauskas <lukas_sabaliauskas@hotmail.com>",
    "version": (0, 0, 2),
    "blender": (4, 0, 0),
    "location": "Object Properties > Relations > Matrix Parent Inverse",
    "warning": "",
    "doc_url": "https://extensions.blender.org/add-ons/reset-workspace/",
    "tracker_url": "https://github.com/Trukasss/ResetWorkspace",
    "category": "User Interface",
}


import bpy
from bpy.types import Context, Operator


class WORKSPACE_OT_reset(Operator):
    """Reset user interface from the default interface"""
    bl_label = "Reset workspace"
    bl_idname = "workspace.reset"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context: Context):
        cls.poll_message_set("Must save current blend file.")
        return bpy.data.is_saved and not bpy.data.is_dirty

    def execute(self, context: Context):
        fp = bpy.data.filepath
        bpy.ops.wm.read_homefile(app_template="", load_ui=True)
        bpy.ops.wm.open_mainfile(filepath=fp, load_ui=False)
        return {"FINISHED"}


def draw_operator(self, context: Context):
    layout = self.layout
    layout.separator()
    layout.operator(WORKSPACE_OT_reset.bl_idname, icon="WORKSPACE")


def register():
    bpy.utils.register_class(WORKSPACE_OT_reset)
    bpy.types.TOPBAR_MT_window.append(draw_operator)


def unregister():
    bpy.utils.unregister_class(WORKSPACE_OT_reset)
    bpy.types.TOPBAR_MT_window.remove(draw_operator)