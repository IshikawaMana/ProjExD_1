import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0

    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False) #左右反転
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0) #10度反時計回転

    bg_rct = bg_img.get_rect()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        bg_rct.move_ip(-1, 0)
        screen.blit(bg_img, bg_rct)

        screen.blit(kk_img, [300, 200])

        tmr += 1        
        clock.tick(200)

        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()