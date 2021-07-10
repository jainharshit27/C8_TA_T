import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 400))

dino_state = "run"
game_state = "play"

score = 0
score_font = pygame.font.Font("freesansbold.ttf", 16)

dino = pygame.image.load("sprites/trex1.png")
cacti = pygame.image.load("sprites/obstacle1.png")
ground = pygame.image.load("sprites/ground.png")

dino_rect = pygame.Rect(100, 250, 64, 64)
cactus_rect = pygame.Rect(1100, 275, 32, 32)
ground_rect = pygame.Rect(0, 330, 1200, 2)

dino_y_change = 0

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_state == "play":
            if dino_state == "run":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dino_y_change = -1
                        jump_sound = pygame.mixer.Sound("sprites/jump.wav")
                        jump_sound.play()
            if dino_state == "jump":
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        dino_y_change = 1
    
        if game_state == "over":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = "play"
                    cactus_rect.x = 1200
                    score = 0
                    dino_y_change = 0
    
    if game_state == "play":
        dino_rect.y += dino_y_change
        if dino_rect.y > 250:
            dino_state = "run"
            dino_rect.y = 250
        if dino_rect.y < 100:
            dino_state = "jump"
            dino_rect.y = 100
            dino_y_change = 1
        
        cactus_rect.x = cactus_rect.x - 1
        if cactus_rect.x <= -30:
            cactus_rect.x = 1200
        
        score += 1
        show_score = round(score/100)
        score_show = score_font.render("Score: " + str(show_score), True, (0, 0, 0))
        screen.blit(score_show, (10, 10))  
        
        screen.blit(dino, dino_rect)
        screen.blit(cacti, cactus_rect)
        
        image_width = ground.get_width()
        screen.blit(ground, ground_rect)
        screen.blit(ground, (image_width + ground_rect.x, ground_rect.y))
        if ground_rect.x <= -image_width:
            screen.blit(ground, (image_width + ground_rect.x, ground_rect.y))
            ground_rect.x = 0
        ground_rect.x -= 1
        
        if dino_rect.colliderect(cactus_rect):
            die_sound = pygame.mixer.Sound("sprites/die.wav")
            die_sound.play()
            pygame.time.delay(500)
            game_state = "over"
            
    if game_state == "over":
        score_show = score_font.render("Score: " + str(show_score), True, (0, 0, 0))
        screen.blit(score_show, (550, 190))
            
    pygame.display.update()
