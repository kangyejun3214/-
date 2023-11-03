from ursina import *
import time
app=Ursina()

combine_parent=Entity(enable=False)

e=Entity(parent=combine_parent,model='plane',origin_y=-.5,texture='white_cube',color=color.orange)
e.look_at(Vec3(1,0,0),'up')

e=Entity(parent=combine_parent,model='plane',origin_y=-.5,texture='white_cube',color=color.white)
e.look_at(Vec3(0,-1,0),'up')

e=Entity(parent=combine_parent,model='plane',origin_y=-.5,texture='white_cube',color=color.yellow)
e.look_at(Vec3(0,1,0),'up')

e=Entity(parent=combine_parent,model='plane',origin_y=-.5,texture='white_cube',color=color.pink)
e.look_at(Vec3(-1,0,0),'up')

e=Entity(parent=combine_parent,model='plane',origin_y=-.5,texture='white_cube',color=color.azure)
e.look_at(Vec3(0,0,1),'up')

e=Entity(parent=combine_parent,model='plane',origin_y=-.5,texture='white_cube',color=color.green)
e.look_at(Vec3(0,0,-1),'up')

combine_parent.combine()
cubes=[]
for x in range(3):
    for y in range(3):
         for z in range(3):
            e=duplicate(combine_parent,position=Vec3(x,y,z)-Vec3(1,1,1),texture='white_cube')
            cubes.append(e)




collider=Entity (model='cube',scale=3,collider='box', visible=False)
def collider_input(key):
    if mouse.hovered_entity == collider :
        if key=='left mouse down' :
             rotate(mouse.normal,1)
        elif key=='right mouse down' :
            rotate(mouse.normal,-1)
collider.input=collider_input

rotation_helper=Entity()

def rotate(normal,direction=1):
    for e in cubes:
        if normal==Vec3(1,0,0)and e.x >0 :
            e.world_parent= rotation_helper

            rotation_helper.animate('rotation_x',90 * direction,duration=0.001)
        elif normal==Vec3(-1,0,0)and e.x <0 :
            e.world_parent= rotation_helper

            rotation_helper.animate('rotation_x',-90 * direction,duration=0.001)


        if normal==Vec3(0,1,0) and e.y >0 :
            e.world_parent= rotation_helper

            rotation_helper.animate('rotation_y', 90 * direction,duration=0.001)
        elif normal==Vec3(0,-1,0) and e.y <0 :
            e.world_parent= rotation_helper

            rotation_helper.animate('rotation_y',-90  * direction,duration=0.001)
    

        if normal==Vec3(0,0,1) and e.z >0 :
            e.world_parent= rotation_helper

            rotation_helper.animate('rotation_z',90 * direction,duration=0.001)
        elif normal==Vec3(0,0,-1) and e.z <0 :
            e.world_parent= rotation_helper

            rotation_helper.animate('rotation_z',-90 * direction,duration=0.001)
    
    
    invoke(reset,delay=0.0011)       
    


def reset():
    for e in cubes:
        e.world_parent=scene
    rotation_helper.rotation=(0,0,0)
def randomize():
    faces = (Vec3(1,0,0), Vec3(0,1,0), Vec3(0,0,1), Vec3(-1,0,0), Vec3(0,-1,0), Vec3(0,0,-1))
    for i in range(2):
        
        rotate(normal=random.choice(faces), direction=random.choice((-1,1)))
        
      
       



randomize_button = Button(text='randomize', color=color.azure, position=(.7,-.4), on_click=randomize)
randomize_button.fit_to_text()

window.color = color.white


EditorCamera()



app.run()



