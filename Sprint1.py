import arcade
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
JUMP_SPEED = 15
GRAVITY = 1
DOT_RADIUS = 20
NUM_DOTS = 10

class Dot(arcade.Sprite):
    def __init__(self):
        super().__init__("Bluedot.png")
        self.center_x = random.randint(50, SCREEN_WIDTH - 50)
        self.center_y = random.randint(50, SCREEN_HEIGHT - 50)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Jumping Game")
        self.player = arcade.Sprite("snake.png")
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.velocity = [0, 0]
        self.score = 0
        self.start_time = 0
        self.dots = arcade.SpriteList()

    def setup(self):
        for _ in range(NUM_DOTS):
            dot = Dot()
            self.dots.append(dot)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.dots.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 20)
        elapsed_time = round(time.time() - self.start_time, 2)
        arcade.draw_text(f"Time: {elapsed_time}", SCREEN_WIDTH - 120, 10, arcade.color.WHITE, 20)

    def update(self, delta_time):
        self.player.update()
        self.dots.update()

        for dot in arcade.check_for_collision_with_list(self.player, self.dots):
            dot.remove_from_sprite_lists()
            self.score += 1

        if self.score >= 10:
            elapsed_time = round(time.time() - self.start_time, 2)
            print(f"Game Over! Score: {self.score}, Time: {elapsed_time}")
            arcade.close_window()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.player.bottom <= 0:
                self.player.change_y = JUMP_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = 0
        elif key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT:
            self.player.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

def main():
    game = MyGame()
    game.setup()
    game.start_time = time.time()
    arcade.run()

if __name__ == "__main__":
    main()
