from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = transform.scale(image.load("background.png"), (700, 500))
player1 = transform.scale(image.load("sprite1.png"), (65, 65))
player2 = transform.scale(image.load("sprite2.png"), (65, 65))
clock = time.Clock()
fps = 60

x = 300
y = 400

x1 = 500
y1 = 400

running = True

while running:
    window.blit(background, (0, 0))
    window.blit(player1, (x, y))
    window.blit(player2, (x1, y1))

    for e in event.get():
        if e.type == QUIT:
            running = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -=3

    if keys_pressed[K_RIGHT] and x1 < 630:
        x1 +=3

    if keys_pressed[K_UP]  and y1 > 5:
        y1 -=3

    if keys_pressed[K_DOWN] and y1 < 430:
        y1 +=3

    if keys_pressed[K_a] and x > 5:
        x -=3

    if keys_pressed[K_d] and x < 630:
        x +=3

    if keys_pressed[K_w] and y > 5:
        y -=3

    if keys_pressed[K_s] and y < 430:
        y +=3

    clock.tick(fps)
    display.update()