import turtle
import random

# Constants
WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 10
DELAY = 100
GRID_SIZE = 20  # Size of the movement grid
offsets = {
    "up": (0, GRID_SIZE),
    "down": (0, -GRID_SIZE),
    "left": (-GRID_SIZE, 0),
    "right": (GRID_SIZE, 0)
}

def reset():
    global snake, snake_direction, food_pos
    snake = [[0, 0], [0, GRID_SIZE], [0, 2 * GRID_SIZE], [0, 3 * GRID_SIZE], [0, 4 * GRID_SIZE]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    move_snake()

def move_snake():
    global snake_direction

    # Next position for the head of the snake
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check self-collision
    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)
        if not food_collision():
            snake.pop(0)  # Remove tail if no food collision

        # Screen wrapping
        if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
        elif snake[-1][0] < -WIDTH / 2:
            snake[-1][0] += WIDTH
        if snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
        elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT

        # Clear previous stamps and draw snake
        pen.clearstamps()
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()
        turtle.ontimer(move_snake, DELAY)

def food_collision():
    global food_pos
    if get_distance(snake[-1], food_pos) < GRID_SIZE:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(-WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# Screen setup
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Pen setup
pen = turtle.Turtle("square")
pen.penup()
pen.pencolor("yellow")

# Food setup
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Start game
reset()
turtle.done()
