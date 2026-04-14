import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    original1 = pg.image.load("fig/pg_bg.jpg")
    flipped1 = pg.transform.flip(original1, True, False)
    
    tmr = 0

    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False) #左右反転
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0) #10度反時計回転

    x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = (x + 1) % 3200

        screen.blit(original1, (-x, 0))
        screen.blit(flipped1, (-x + 1600, 0))
        screen.blit(original1, (-x + 3200, 0))
        
        screen.blit(kk_img, [300, 200])

        tmr += 1        
        clock.tick(200)

        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()