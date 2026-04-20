import pygame
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Game")

# Fonts
font1 = pygame.font.SysFont('Arial', 20, bold=True)  
font2 = pygame.font.SysFont('Arial', 40, bold=True) 

# Colours
bg_color = (11, 14, 20)
snake_color1 = (50,	243, 255, 255)
snake_color2 = (139,172,15,255)
food_color = (255, 0, 122, 255)
text_color = (255, 255, 255, 255)
bonus_color = (244, 179, 66, 255)

# bg_color = (48,98,48)
# snake_color1 = (139,172,15,255)
# food_color = (155,188,15,255)
# text_color = (15,56,15,255)

# bg_color = (46, 52, 64)
# snake_color1 = (163, 190, 140, 255)
# food_color = (208, 135, 112, 255)
# text_color = (236, 239, 244, 255)


running = True
clock = pygame.time.Clock()

text_won1 = font2.render("Player 1 Won!", True,
            pygame.Color(248, 187, 102, 225))
text_won2 = font2.render("Player 2 Won!", True,
            pygame.Color(248, 187, 102, 225))

# Snake Discription
snake_size = 20

x_pos1 = 100
y_pos1 = 200
x_step1 = 0
y_step1 = -20
body1 = []

x_pos2 = 300
y_pos2 = 200
x_step2 = 0
y_step2 = -20
body2 = []

# Food Discription
food_size = 20
x_food = random.randint(0, 400-snake_size)
y_food = random.randint(20, 400-snake_size)
x_food = x_food - x_food%20
y_food = y_food - y_food%20

x_bonus = 0
y_bonus = 0

player1 =0
player2 =0
winner =0

print("   W")
print("A  S  D      for player 1\n")
print("   ^")
print("<  ⌄  >      for player 2")
print("\n   Enjoy Competing!")


while(running):

    for event in pygame.event.get():

        if event.type == pygame.QUIT or pygame.KEYDOWN == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()

            # Check for key movements
            # Player 1
            if event.key == pygame.K_w and y_step1!=snake_size:
                y_step1 = -snake_size
                x_step1 = 0
            if event.key == pygame.K_s and y_step1!=-snake_size:
                y_step1 = snake_size
                x_step1 = 0
            if event.key == pygame.K_a and x_step1!=snake_size:
                x_step1 = -snake_size
                y_step1 = 0
            if event.key == pygame.K_d and x_step1!=-snake_size:
                x_step1 = snake_size
                y_step1 = 0
            
            # Player 2
            if event.key == pygame.K_UP and y_step2!=snake_size:
                y_step2 = -snake_size
                x_step2 = 0
            if event.key == pygame.K_DOWN and y_step2!=-snake_size:
                y_step2 = snake_size
                x_step2 = 0
            if event.key == pygame.K_LEFT and x_step2!=snake_size:
                x_step2 = -snake_size
                y_step2 = 0
            if event.key == pygame.K_RIGHT and x_step2!=-snake_size:
                x_step2 = snake_size
                y_step2 = 0

            #####       for Debugging       #####
            
            # Press 1 to increase score od player 1 by 1  
            if(event.key == pygame.K_1):
                x_food = random.randint(0, 400-snake_size)
                y_food = random.randint(20, 400-snake_size)
                x_food = x_food - x_food%20
                y_food = y_food - y_food%20
                if(len(body1)>0):
                    body1.append([body1[len(body1)-1][0], body1[len(body1)-1][1]])
                    body1.append([body1[len(body1)-1][0], body1[len(body1)-1][1]])
                else:
                    body1.append([x_pos1, y_pos1])
                    body1.append([x_pos1, y_pos1])
                print("Hit")
                print("score (player1): ", player1)
                player1 += 1

            # Press 1 to increase score od player 1 by 1  
            if(event.key == pygame.K_2):
                x_food = random.randint(0, 400-snake_size)
                y_food = random.randint(20, 400-snake_size)
                x_food = x_food - x_food%20
                y_food = y_food - y_food%20
                if(len(body2)>0):
                    body2.append([body2[len(body2)-1][0], body2[len(body2)-1][1]])
                    body2.append([body2[len(body2)-1][0], body2[len(body2)-1][1]])
                else:
                    body2.append([x_pos2, y_pos2])
                    body2.append([x_pos2, y_pos2])
                print("Hit")
                print("score (player2): ", player2)
                player2 += 1

    # Render Bonus Food
    i = random.randint(1, 10)
    if(i==5 and (x_bonus==0 and y_bonus==0)):
        x_bonus = random.randint(20, 400-snake_size)
        y_bonus = random.randint(20, 400-snake_size)
        x_bonus = x_bonus - x_bonus%20
        y_bonus = y_bonus - y_bonus%20

    if(x_bonus!=0 and y_bonus!=0):
        pygame.draw.rect(screen, bonus_color, pygame.Rect((x_bonus, y_bonus), (food_size, food_size)))

    # Head hits Bonus
    if(x_pos1==x_bonus and y_pos1==y_bonus):
        if(len(body1)>0):
            body1.append([body1[len(body1)-1][0], body1[len(body1)-1][1]])
            body1.append([body1[len(body1)-1][0], body1[len(body1)-1][1]])
            body1.append([body1[len(body1)-1][0], body1[len(body1)-1][1]])
        else:
            body1.append([x_pos1, y_pos1])
            body1.append([x_pos1, y_pos1])
            body1.append([x_pos1, y_pos1])
        print("Hit")
        player1 += 3
        print("score (player1): ", player1)
        x_bonus=0
        y_bonus=0
    if(x_pos2==x_bonus and y_pos2==y_bonus):
        if(len(body2)>0):
            body2.append([body2[len(body2)-1][0], body2[len(body2)-1][1]])
            body2.append([body2[len(body2)-1][0], body2[len(body2)-1][1]])
            body2.append([body2[len(body2)-1][0], body2[len(body2)-1][1]])
        else:
            body2.append([x_pos2, y_pos2])
            body2.append([x_pos2, y_pos2])
            body2.append([x_pos2, y_pos2])
        print("Hit")
        player2 += 3
        print("score (player2): ", player2)
        x_bonus=0
        y_bonus=0

    # Head hitd food
    if(x_pos1==x_food and y_pos1==y_food):
        x_food = random.randint(0, 400-snake_size)
        y_food = random.randint(20, 400-snake_size)
        x_food = x_food - x_food%20
        y_food = y_food - y_food%20

        if(len(body1)>0):
            body1.append([body1[len(body1)-1][0], body1[len(body1)-1][1]])
        else:
            body1.append([x_pos1, y_pos1])
        print("Hit")
        player1 += 1
        print("score (player1): ", player1)
    if(x_pos2==x_food and y_pos2==y_food):
        x_food = random.randint(0, 400-snake_size)
        y_food = random.randint(20, 400-snake_size)
        x_food = x_food - x_food%20
        y_food = y_food - y_food%20

        if(len(body2)>0):
            body2.append([body2[len(body2)-1][0], body2[len(body2)-1][1]])
        else:
            body2.append([x_pos2, y_pos2])
        print("Hit")
        player2 += 1
        print("score (player2): ", player2)

    # Update the position of each body block
    if(len(body1)>0):
        body1[0] = [x_pos1, y_pos1]
        for i in range(len(body1)-1, 0, -1):
            #print("hi")
            body1[i] = body1[i-1]
    if(len(body2)>0):
        body2[0] = [x_pos2, y_pos2]
        for i in range(len(body2)-1, 0, -1):
            #print("hi")
            body2[i] = body2[i-1]

    # Update the position of head
    x_pos1 += x_step1
    y_pos1 += y_step1
    if(x_pos1>400-snake_size):
        x_pos1=0
    if(x_pos1<0):
        x_pos1=400-snake_size
    if(y_pos1>400-snake_size):
        y_pos1=0
    if(y_pos1<0):
        y_pos1=400-snake_size

    x_pos2 += x_step2
    y_pos2 += y_step2
    if(x_pos2>400-snake_size):
        x_pos2=0
    if(x_pos2<0):
        x_pos2=400-snake_size
    if(y_pos2>400-snake_size):
        y_pos2=0
    if(y_pos2<0):
        y_pos2=400-snake_size

    for b in body1:
        # Checking Collision of head with own body
        if(x_pos1==b[0] and y_pos1==b[1] and not winner):
            winner = 2
            #screen.blit(text_won2, (70, 160))
            x_step1 = 0 
            y_step1 = 0
            x_step2 = 0
            y_step2 = 0
        # Checking collision of enemy head with player1 body
        if(x_pos2==b[0] and y_pos2==b[1] and not winner):
            winner = 1
            x_step1 = 0 
            y_step1 = 0
            x_step2 = 0
            y_step2 = 0
        # Rendering 'b'th body block
        pygame.draw.rect(screen, snake_color1, pygame.Rect((b[0], b[1]), (snake_size, snake_size)))
        
    for b in body2:
        # Checking Collision of body block with Head
        if(x_pos2==b[0] and y_pos2==b[1] and not winner):
            winner = 1
            #screen.blit(text_won1, (70, 160))
            x_step2 = 0 
            y_step2 = 0
            x_step1 = 0
            y_step1 = 0
        # Checking collision of enemy head with player2 body
        if(x_pos1==b[0] and y_pos1==b[1] and not winner):
            winner = 1
            x_step1 = 0 
            y_step1 = 0
            x_step2 = 0
            y_step2 = 0

        # Rendering 'b'th body block
        pygame.draw.rect(screen, snake_color2, pygame.Rect((b[0], b[1]), (snake_size, snake_size)))
    
    # Render the Food
    pygame.draw.rect(screen, food_color, pygame.Rect((x_food, y_food), (food_size, food_size)))

    # Render the Head
    pygame.draw.rect(screen, snake_color1, pygame.Rect((x_pos1, y_pos1), (snake_size, snake_size)))
    pygame.draw.rect(screen, snake_color2, pygame.Rect((x_pos2, y_pos2), (snake_size, snake_size)))

    # Render Highscores and Score
    text_score1 = font1.render(f"Player 1: {player1}", True,
            pygame.Color(snake_color1),
            pygame.Color(bg_color))
    text_score2 = font1.render(f"Player 2: {player2}", True,
            pygame.Color(snake_color2),
            pygame.Color(bg_color))
    if(winner>0):
        if(winner == 1):
            screen.blit(text_won1, (70, 160))
        else:
            screen.blit(text_won2, (70, 160))
    screen.blit(text_score1, (0,0))
    screen.blit(text_score2, (285,0))

    # Game tick and screen update
    clock.tick(3)
    pygame.display.flip()
    screen.fill(bg_color)

pygame.quit()