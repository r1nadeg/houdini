houdini
import hou from nodesearch import parser

copying celected nodes to custom list
ren_nodes = [] print("The following nodes are currently selected:") for ren_node in hou.selectedNodes():
ren_nodes.append(ren_node) print(ren_node)

bining ver_node to node with version controls
print ("hou.paneTabType.NetworkEditor", hou.paneTabType.NetworkEditor) editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor) print("editor", editor) ver_node = parser.select("v* find_me=1", editor=editor, frame=True) print("ver_node: ", ver_node)

#Attempt to make a node creator -- failed

if (ver_node == None): #print("Creating version control node") #desktop = hou.ui.curDesktop() #desktop.paneUnderCursor() #print("hou.ui.desktops", hou.ui.desktops()) #print("desktop.paneUnderCursor()", desktop.paneUnderCursor()) ren_node = hou.selectedNodes()[0] path = ren_node.path() context = path.rpartition('/')[0]

obj = hou.node(context)
obj.createNode("v0000")
ver_node = parser.select("v* find_me=1", editor=editor, frame=True)
""" hasNetworkControls() → bool

Return True if this pane tab type supports network controls.

cd(path)

"""

for ren_node in ren_nodes:

ren_node_name = ren_node.name()
i = 0
for node in hou.selectedNodes():
    try:
        ver_ctrl = hou.node(node.path())
        link = ver_ctrl.parm("ver_name").path()
        
        path = r'$HIP/render/%NAME%_`chs("%LINK%")`/%NAME%_`chs("%LINK%")`.$F4.exr'
        #path = r'$HIP/render/%NAME%_`chs("%LINK%")`_%NAME%_`chs("%LINK%")`.$F4.exr'
        
        print ("Link: ", link)
        print("Source path: ", path)    
        tmp_path = path.replace("%LINK%", link)
        res_path = tmp_path.replace("%NAME%", ren_node_name)
        print("Result path: ", res_path)
        ren_node.parm("vm_picture").set(res_path)
        node.parm("ver_name")
        print("i=", i, "selected: ", node.path())
        node = hou.selectedNodes(i)
        print(node)
        print(hou.pwd())
        i += 1
    except:
        print("\n\nThe selection most likely is wrong!\nSelect mantra render nodes\n\n")
#else:

print ("Nothing is selected!")
