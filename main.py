import pygame
import math

class Gim:
    def __init__(self):
        self.run_game()

    def load_image_player(self):
        self.img_player = pygame.image.load("assets/people.png")
        self.screen.blit(self.img_player, (self.x_player, self.y_player))

    def load_image_ninja(self):
        self.img_ninja = pygame.image.load("assets/leonardo.png")
        self.screen.blit(self.img_ninja, (self.x_ninja, self.y_ninja))

    def load_image_meteor(self):
        self.img_meteor = pygame.image.load("assets/meteor.png")
        self.screen.blit(self.img_meteor, (self.x_meteor, self.y_meteor))

    def collition_detection(self, x1, x2, y1, y2):
        self.distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return self.distance < 10

    def run_game(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 500))
        pygame.display.set_caption("Game Sederhana")

        self.bg_img = pygame.image.load("assets/Background.png")
        self.bg = pygame.transform.scale(self.bg_img, (1000, 500))

        # player
        self.x_player = 50
        self.y_player = 435
        self.vel_player = 7
        self.damage = 20
        self.is_jumping = False
        self.jump_vel = 10
        self.gravity = 0.5

        # ninja
        self.x_ninja = 950
        self.y_ninja = 435
        self.vel_ninja = 1
        self.x_point_ninja = 0
        self.health = 500

        # meteor
        self.x_meteor = 0
        self.y_meteor = 0
        self.vel_meteor = 4
        self.meteor_nembak = False

        self.running = True
        while self.running:
            self.screen.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            key = pygame.key.get_pressed()

            if (key[pygame.K_LEFT] or key[ord("a")]) and self.x_player > 0:
                self.x_player -= self.vel_player

            if (key[pygame.K_RIGHT] or key[ord("d")]) and self.x_player < 950:
                self.x_player += self.vel_player

            if not self.is_jumping:
                if key[pygame.K_SPACE]:
                    self.is_jumping = True
                    self.jump_vel = -10

            if self.is_jumping:
                self.y_player += self.jump_vel
                self.jump_vel += self.gravity
                if self.y_player >= 435:  # Reset position after landing
                    self.y_player = 435
                    self.is_jumping = False

            if key[ord("q")]:
                self.meteor_nembak = True
                self.x_meteor = self.x_player
                self.y_meteor = self.y_player

            if self.x_ninja <= 120:
                self.x_point_ninja += self.vel_ninja

            if self.x_ninja >= 950:
                self.x_point_ninja -= self.vel_ninja

            if self.meteor_nembak:
                self.load_image_meteor()
                self.x_meteor += (self.vel_meteor + 2)

                if self.collition_detection(self.x_ninja, self.x_meteor, self.y_ninja, self.y_meteor):
                    self.health -= self.damage
                    print(f"Hit!! damage = {self.damage}, health {self.health}")
                    self.meteor_nembak = False

            if self.collition_detection(self.x_player, self.x_ninja, self.y_player, self.y_ninja):
                print("Anda tertangkap Ninja!, Anda kalah.")
                break

            if self.health < 0:
                print("Anda menang!")
                break

            self.x_ninja += self.x_point_ninja

            self.load_image_player()
            self.load_image_ninja()
            pygame.display.update()

if __name__ == "__main__":
    Gim()
