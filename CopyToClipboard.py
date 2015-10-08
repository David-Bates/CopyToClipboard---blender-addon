bl_info = {
	"name": "Copy To Clipboard",
	"description": "A simple tool to add the ability to copy text objects' text to the system clipboard.",
	"author": "David Bates",
	"blender": (2, 7, 0),
	"location": "3D View Header > Edit > Copy To Clipboard",
	"category": "3D View",
}

import bpy

class CopyToClipboard(bpy.types.Operator):
	"""Copy to system clipboard"""
	bl_idname = "font.text_copy_to_clipboard"
	bl_label = "Copy To Clipboard"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		# The script
		ob = context.active_object
		context.window_manager.clipboard = ob.data.body

		return {'FINISHED'}

def register():
	bpy.utils.register_class(CopyToClipboard)
	bpy.types.VIEW3D_MT_select_edit_text.append(menu_draw)

def unregister():
	bpy.utils.unregister_class(CopyToClipboard)


def menu_draw(self, context):
	self.layout.operator(CopyToClipboard.bl_idname)

if __name__ == "__main__":
	register()