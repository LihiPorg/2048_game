import pygame
import sys
import random

pygame.init()   #creates a pygame object

width=400
hight=400

RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
COLOR2=(255, 160, 122)
COLOR4= (250, 128, 114)
COLOR8=(205, 92, 92)
COLOR16=(255, 192, 203)
COLOR32=(255, 127, 80)
COLOR64=(202,127,174)
COLOR128 = (255, 223, 186)  
COLOR256 = (255, 204, 153)  
COLOR512 = (255, 178, 102)  
COLOR1024 = (255, 153, 51)  
COLOR2048 = (255, 128, 0)   
end=False
player_size=[int(width/4),int(hight/4)]
cube_list=[]
speed=10
screen=pygame.display.set_mode((width,hight))      
game_over=False
score=0
clock= pygame.time.Clock()
myfont=pygame.font.SysFont("monospace",35)

def make_board(width,hight): #creates empty board
	bhight=hight
	while width>=0:
		while hight>=0:
			pygame.draw.rect(screen,WHITE, (width,hight,player_size[0],player_size[1]),2)
			hight-=player_size[1]
		width-=player_size[0]
		hight=bhight

def add_cube(width,hight,cube_list,player_size): #adds a cube at the end of each play, if there is no space to add cube the player lose
	original=len(cube_list)
	if(len(cube_list)<16):
		while original==len(cube_list):
			c_x=random.choice(range(0,width+1-player_size[0],player_size[0]))
			c_y=random.choice(range(0,hight+1-player_size[1],player_size[1]))
			if [cube for cube in cube_list if (cube[0]==c_x and cube[1]==c_y)]==[]:
				text= str(random.choice(range(2,5,2)))
				cube_list=cube_sort(cube_list,[c_x,c_y,text])
		return cube_list
	else:
		display_message("You Lose :(")

def cube_sort(cube_list,cube): 
	cube_list.append(cube)
	cube_list=sorted(cube_list,key=lambda k: [k[1],k[0]])
	return cube_list

def draw_cubes(cube_list,player_size):
	for cube in cube_list:

		pygame.draw.rect(screen,eval("COLOR"+str(cube[2])), (cube[0],cube[1],player_size[0],player_size[1]))
		
		label=myfont.render(str(cube[2]),1,BLACK)
		screen.blit(label,(cube[0],cube[1]))
		


def move_left(cube_list,player_size):
	global end
	current_x=0
	current_y=0
	cubee_list=cube_list
	for idx,cube in enumerate(cube_list[:]):
		if cube[1]!=current_y:
		 	current_y=cube[1]
		 	current_x=0
		 	cube_list[idx]=[current_x,current_y,cube[2]]
		 	current_x+=player_size[0]
		else:
			# ex_x=cube_list[idx][0]
			cube_list[idx]=[current_x,current_y,cube[2]]
			current_x=cube_list[idx][0]+player_size[0]
			if idx!=0:
			 	before_cube=cube_list[idx-1]
			 	if(int(before_cube[2])==int(cube[2])):
			 		cube_list[idx-1][2]=int(cube[2])*2
			 		if cube_list[idx-1][2]==2048:
			 			end=True
			 		cube_list[idx][2]=0
			 		current_x=before_cube[0]+player_size[0]
			 

	cube_list[:]=(x for x in cube_list if x[2]!=0)
	return cube_list

def move_right(cube_list,player_size):
	global end
	current_x=width-player_size[0]
	current_y=0
	cube_list.reverse()
	for idx,cube in enumerate(cube_list):
		if cube[1]!=current_y:
		 	current_y=cube[1]
		 	current_x=width-player_size[0]
		 	cube_list[idx]=[current_x,current_y,cube[2]]
		 	current_x-=player_size[0]
		else:
			cube_list[idx]=[current_x,current_y,cube[2]]
			current_x-=player_size[0]
			if idx!=0:
				before_cube=cube_list[idx-1]
				if(int(before_cube[2])==int(cube[2])):
					cube_list[idx-1][2]=int(cube[2])*2
					if cube_list[idx-1][2]==2048:
			 			end=True
					cube_list[idx][2]=0
					current_x=before_cube[0]-player_size[0]
	cube_list[:]=(x for x in cube_list if x[2]!=0)
	return cube_list

def move_up(cube_list, player_size):
	global end
	current_x = 0
	current_y = 0
	cube_list = sorted(cube_list, key=lambda k: [k[0], k[1]])  # Sort by x first, then by y
	for idx, cube in enumerate(cube_list):
	    if cube[0] != current_x:
	        current_x = cube[0]
	        current_y = 0
	        cube_list[idx] = [current_x, current_y, cube[2]]
	        current_y += player_size[1]
	    else:
	        cube_list[idx] = [current_x, current_y, cube[2]]
	        current_y += player_size[1]
	        if idx != 0:
	            before_cube = cube_list[idx - 1]
	            if int(before_cube[2]) == int(cube[2]):
	                cube_list[idx - 1][2] = int(cube[2]) * 2
	                if cube_list[idx - 1][2] == 2048:
	                    end = True 
	                cube_list[idx][2] = 0
	                current_y = before_cube[1] + player_size[1]

	cube_list[:] = [x for x in cube_list if x[2] != 0]
	return cube_list


def move_down(cube_list, player_size):
	global end
	current_x = 0
	current_y = hight - player_size[1]
	cube_list = sorted(cube_list, key=lambda k: [k[0], -k[1]])  # Sort by x first, then by y in descending order
	for idx, cube in enumerate(cube_list):
	    if cube[0] != current_x:
	        current_x = cube[0]
	        current_y = hight - player_size[1]  
	        cube_list[idx] = [current_x, current_y, cube[2]]
	        current_y -= player_size[1]
	    else:
	        cube_list[idx] = [current_x, current_y, cube[2]]
	        current_y -= player_size[1]
	        if idx != 0:
	            before_cube = cube_list[idx - 1]
	            if int(before_cube[2]) == int(cube[2]):
	                cube_list[idx - 1][2] = int(cube[2]) * 2
	                if cube_list[idx - 1][2] == 2048:
	                    end = True  
	                cube_list[idx][2] = 0
	                current_y = before_cube[1] - player_size[1]
	cube_list[:] = [x for x in cube_list if x[2] != 0]
	return cube_list

def display_message(msg):
	screen.fill(BLACK)  
	draw_cubes(cube_list, player_size)  
	make_board(width, hight)  
	pygame.display.update() 
	pygame.time.wait(1000)
	screen.fill(BLACK)  
	label = myfont.render(msg, 1, WHITE)  
	screen.blit(label, (width // 2 - label.get_width() // 2, hight // 2 - label.get_height() // 2))  
	pygame.display.update()  
	pygame.time.wait(3000)  
	pygame.quit()
	sys.exit()

cube_list=add_cube(width,hight,cube_list,player_size)
cube_list=add_cube(width,hight,cube_list,player_size)
draw_cubes(cube_list,player_size)
make_board(width,hight)
pygame.display.update()

while not game_over:

		for event in pygame.event.get(): 

			if event.type==pygame.QUIT:             
				sys.exit()

			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					cube_list=move_left(cube_list,player_size)
				elif event.key==pygame.K_RIGHT:
					cube_list=move_right(cube_list,player_size)
				elif event.key==pygame.K_DOWN:
					cube_list=move_down(cube_list,player_size)
				elif event.key==pygame.K_UP:
					cube_list=move_up(cube_list,player_size)
				cube_list=add_cube(width,hight,cube_list,player_size)
				draw_cubes(cube_list,player_size)
				make_board(width,hight)
				pygame.display.update()
				if end:
					display_message("You Won :)")


				
		screen.fill(BLACK)
		clock.tick(10)