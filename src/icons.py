import bpy.utils.previews
from pathlib import Path


_icons = {}


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    icons_dir = Path(__file__).parent / "images"
    _icons.load(
        name="reset", 
        path=str(icons_dir / "icon_reset.png"), 
        path_type="IMAGE")


def unregister():
    bpy.utils.previews.remove(_icons)


def get_reset_id():
    return _icons["reset"].icon_id