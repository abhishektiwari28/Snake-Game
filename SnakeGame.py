import turtle
import random
import time
import os

# Game Constants
WIDTH = 600
HEIGHT = 600
FOOD_SIZE = 20
MOVE_DISTANCE = 20
INITIAL_DELAY = 0.15
SCORE_INCREMENT = 10
HIGH_SCORE_FILE = "high_score.txt"

class SnakeGame:
    def __init__(self):
        self.delay = INITIAL_DELAY
        self.score = 0
        self.high_score = self.load_high_score()
        self.game_state = "start"  # start, playing, paused, game_over
        self.bodies = []
        
        # Setup screen
        self.setup_screen()
        
        # Create game objects
        self.create_snake()
        self.create_food()
        self.create_scoreboard()
        self.create_text_display()
        
        # Setup controls
        self.setup_controls()
        
        # Show start screen
        self.show_start_screen()
    
    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.title("🐍 Enhanced Snake Game")
        self.screen.bgcolor("#1a1a2e")
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.tracer(0)
    
    def create_snake(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("#00ff41")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"
    
    def create_food(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("#ff6b6b")
        self.food.penup()
        self.place_food()
    
    def create_scoreboard(self):
        self.scoreboard = turtle.Turtle()
        self.scoreboard.speed(0)
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(-290, 260)
        self.update_scoreboard()
    
    def create_text_display(self):
        self.text_display = turtle.Turtle()
        self.text_display.speed(0)
        self.text_display.color("white")
        self.text_display.penup()
        self.text_display.hideturtle()
        self.text_display.goto(0, 0)
    
    def load_high_score(self):
        try:
            if os.path.exists(HIGH_SCORE_FILE):
                with open(HIGH_SCORE_FILE, 'r') as file:
                    return int(file.read().strip())
        except:
            pass
        return 0
    
    def save_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, 'w') as file:
                file.write(str(self.high_score))
        except:
            pass
    
    def show_start_screen(self):
        self.text_display.clear()
        self.text_display.goto(0, 50)
        self.text_display.write("🐍 SNAKE GAME 🐍", align="center", font=("Arial", 24, "bold"))
        self.text_display.goto(0, 0)
        self.text_display.write("Press SPACE to Start", align="center", font=("Arial", 16, "normal"))
        self.text_display.goto(0, -30)
        self.text_display.write("Use Arrow Keys to Move", align="center", font=("Arial", 12, "normal"))
        self.text_display.goto(0, -50)
        self.text_display.write("Press P to Pause", align="center", font=("Arial", 12, "normal"))
    
    def show_game_over_screen(self):
        self.text_display.clear()
        self.text_display.goto(0, 50)
        self.text_display.write("GAME OVER!", align="center", font=("Arial", 24, "bold"))
        self.text_display.goto(0, 10)
        self.text_display.write(f"Final Score: {self.score}", align="center", font=("Arial", 16, "normal"))
        self.text_display.goto(0, -20)
        self.text_display.write("Press SPACE to Play Again", align="center", font=("Arial", 14, "normal"))
        self.text_display.goto(0, -50)
        self.text_display.write("Press Q to Quit", align="center", font=("Arial", 12, "normal"))
    
    def show_pause_screen(self):
        self.text_display.clear()
        self.text_display.goto(0, 0)
        self.text_display.write("PAUSED", align="center", font=("Arial", 24, "bold"))
        self.text_display.goto(0, -30)
        self.text_display.write("Press P to Resume", align="center", font=("Arial", 14, "normal"))
    
    def place_food(self):
        while True:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            # Make sure food doesn't spawn on snake
            food_pos = (x, y)
            snake_positions = [(self.head.xcor(), self.head.ycor())]
            snake_positions.extend([(body.xcor(), body.ycor()) for body in self.bodies])
            
            if not any(abs(food_pos[0] - pos[0]) < FOOD_SIZE and abs(food_pos[1] - pos[1]) < FOOD_SIZE for pos in snake_positions):
                self.food.goto(x, y)
                break
    
    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score} | High Score: {self.high_score}", 
                            font=("Arial", 16, "normal"))
    
    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.move_up, "Up")
        self.screen.onkey(self.move_down, "Down")
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
        self.screen.onkey(self.toggle_pause, "p")
        self.screen.onkey(self.start_game, "space")
        self.screen.onkey(self.quit_game, "q")
    
    def move_up(self):
        if self.game_state == "playing" and self.head.direction != "down":
            self.head.direction = "up"
    
    def move_down(self):
        if self.game_state == "playing" and self.head.direction != "up":
            self.head.direction = "down"
    
    def move_left(self):
        if self.game_state == "playing" and self.head.direction != "right":
            self.head.direction = "left"
    
    def move_right(self):
        if self.game_state == "playing" and self.head.direction != "left":
            self.head.direction = "right"
    
    def toggle_pause(self):
        if self.game_state == "playing":
            self.game_state = "paused"
            self.show_pause_screen()
        elif self.game_state == "paused":
            self.game_state = "playing"
            self.text_display.clear()
    
    def start_game(self):
        if self.game_state in ["start", "game_over"]:
            self.reset_game()
            self.game_state = "playing"
            self.text_display.clear()
    
    def quit_game(self):
        if self.game_state == "game_over":
            self.screen.bye()
    
    def reset_game(self):
        self.score = 0
        self.delay = INITIAL_DELAY
        self.head.goto(0, 0)
        self.head.direction = "stop"
        
        # Clear snake body
        for body in self.bodies:
            body.hideturtle()
        self.bodies.clear()
        
        # Reset food position
        self.place_food()
        self.update_scoreboard()
    
    def move_snake(self):
        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + MOVE_DISTANCE)
        elif self.head.direction == "down":
            self.head.sety(self.head.ycor() - MOVE_DISTANCE)
        elif self.head.direction == "left":
            self.head.setx(self.head.xcor() - MOVE_DISTANCE)
        elif self.head.direction == "right":
            self.head.setx(self.head.xcor() + MOVE_DISTANCE)
    
    def check_wall_collision(self):
        return (self.head.xcor() > 290 or self.head.xcor() < -290 or 
                self.head.ycor() > 290 or self.head.ycor() < -290)
    
    def check_body_collision(self):
        for body in self.bodies:
            if self.head.distance(body) < 20:
                return True
        return False
    
    def check_food_collision(self):
        return self.head.distance(self.food) < 20
    
    def add_body_segment(self):
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("#4ecdc4")
        body.penup()
        self.bodies.append(body)
    
    def move_body(self):
        # Move body segments
        for i in range(len(self.bodies) - 1, 0, -1):
            x = self.bodies[i - 1].xcor()
            y = self.bodies[i - 1].ycor()
            self.bodies[i].goto(x, y)
        
        # Move first body segment to head position
        if self.bodies:
            x = self.head.xcor()
            y = self.head.ycor()
            self.bodies[0].goto(x, y)
    
    def game_over(self):
        self.game_state = "game_over"
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
            self.update_scoreboard()
        self.show_game_over_screen()
    
    def run(self):
        while True:
            self.screen.update()
            
            if self.game_state == "playing":
                # Move snake body first
                self.move_body()
                
                # Then move head
                self.move_snake()
                
                # Check wall collision
                if self.check_wall_collision():
                    self.game_over()
                    continue
                
                # Check body collision
                if self.check_body_collision():
                    self.game_over()
                    continue
                
                # Check food collision
                if self.check_food_collision():
                    self.place_food()
                    self.add_body_segment()
                    self.score += SCORE_INCREMENT
                    
                    # Increase speed slightly
                    if self.delay > 0.08:
                        self.delay -= 0.001
                    
                    # Update high score if needed
                    if self.score > self.high_score:
                        self.high_score = self.score
                    
                    self.update_scoreboard()
                
                time.sleep(self.delay)
            else:
                time.sleep(0.1)

# Run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run()