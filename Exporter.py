import bpy

import bpy
import bmesh

def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 



outputFile = 'D:/anim_flower1.px'

depsgraph = bpy.context.evaluated_depsgraph_get()

frame_start = bpy.context.scene.frame_start
frame_end = bpy.context.scene.frame_end

csvLines = "# START "


for frame_number in range(frame_start, frame_end+1):
    bpy.context.scene.frame_set(frame_number)
    #bpy.ops.object.modifier_apply(modifier="ParticleInstance")
    obj = bpy.data.objects['Vertex']

    bm = bmesh.new()

    bm.from_object( obj, depsgraph )

    bm.verts.ensure_lookup_table()

    print( "\n-frame-" )
    verts = [ v.co for v in bm.verts ]
    csvLines = csvLines+"# FRAME "
    csvLinesTemp = [ "Pa "+(" ".join([str(v) for v in co ])) + "\n" for co in verts ]
    csvLines = csvLines+"\n"+''.join([str(elem) for elem in csvLinesTemp]) 
    bm.free()


f = open( outputFile, 'w' )
f.writelines( csvLines )
f.close()