# Space Invaders.py
import turtle as trtl
import math
import random as rand

"""
Things needed for the screen
"""

wn = trtl.Screen()

# Make the background and title
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("outerspace.gif")
wn.tracer(0)

# border set up
border = trtl.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-300,-300)
border.pendown()
border.pensize(3)

# border
for i in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()

# Score
score = 0

# Score Writer
score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.color("white")
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-290, 260)
score_writer.pendown()

font_setup = ("Arial", "15", "normal")
score_writer.write(str(score) + " points", font = font_setup)

# Update score function
def update_score():
  score_writer.clear()
  global score
  score += 10
  score_writer.write(str(score) + " points", font = font_setup)

# player
p = trtl.Turtle()
p.speed(0)
p.color("blue")
p.shape("triangle")
p.penup()
p.goto(0,-250)
p.setheading(90)

player_speed = 15

# move the player left and right
def move_left():
    x = p.xcor()
    x -= player_speed
    # if it goes out of boundaries
    if x < -280:
        x = -280
    p.setx(x)

def move_right():
    x = p.xcor()
    x += player_speed
    # if it goes out of boundaries
    if x > 280:
        x = 280
    p.setx(x)

# def gun
def fire_gun():
    global gunstate 
    # if the gunstate is ready then it fires
    if gunstate == "ready":
        gunstate = "fire"
        # Move the bullet
        x = p.xcor()
        y = p.ycor() + 10
        g.goto(x,y)
        g.showturtle()

# is Collision
def hit(player1,player2):
    # check the collision
    distance = math.sqrt(math.pow(player1.xcor() - player2.xcor(),2) + math.pow(player1.ycor() - player2.ycor(),2))
    
    if distance < 15:
        return True
    else:
        return False 

# gun
g = trtl.Turtle()
g.speed(0)
g.color("yellow")
g.shape("triangle")
g.penup()
g.setheading(90)
g.shapesize(0.5,0.5)
g.hideturtle()

gun_speed = 10


# ready to fire
# fire
gunstate = "ready"

# keyboard
wn.listen()
wn.onkey(move_left, "a")
wn.onkey(move_right, "d")
wn.onkey(fire_gun, "space")

# Number of Enemies
num_of_enemies = 30

# Create list
enemies = []
e = trtl.Turtle()

# Add enemies to the list
for i in range(num_of_enemies):
    # Create the enemies
    enemies.append(trtl.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_num = 0

# enemy
for e in enemies:
    e.speed(0)
    e.color("red")
    e.shape("circle")
    e.penup()
    e.speed(0)
    x = enemy_start_x + 50 * enemy_num
    y = enemy_start_y 
    e.goto(x,y)
    # Update enemy number 
    enemy_num += 1
    if enemy_num == 10:
        enemy_start_y -= 50
        enemy_num = 0

enemy_speed = 0.2

# While the game is still running-
while True:
    wn.update()
    for e in enemies:
        # Move enemy
        x = e.xcor()
        x += enemy_speed
        e.setx(x)

        # Move the enemy back/down
        if e.xcor() > 280:
            # Move all enemies down
            for enemy in enemies:
                y = enemy.ycor()
                y -= 40
                enemy.sety(y)
            # Change direction
            enemy_speed *= -1

        elif e.xcor() < -280:
            # Move all enemies down
            for enemy in enemies:
                y = enemy.ycor()
                y -= 40
                enemy.sety(y)
            # Change direction
            enemy_speed *= -1

         # if bullet goes to top
        if g.ycor() > 275:
            g.hideturtle()
            gunstate = "ready"

        # Check collision for gun/enemy
        if hit(g,e):
            # Reset Gun
            g.hideturtle()
            gunstate = "ready"
            g.goto(0,-400)
            # Reset Enemy
            e.goto(0,10000)
            
            # Update score
            update_score()

        # Game over
        if hit(p,e):
            p.hideturtle()
            e.hideturtle()
            break

    # Move bullet
    y = g.ycor()
    y += gun_speed
    g.sety(y)

wn.mainloop()
