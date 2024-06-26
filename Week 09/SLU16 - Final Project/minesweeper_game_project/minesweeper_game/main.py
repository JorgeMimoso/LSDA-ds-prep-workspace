"""
    PLEASE DO NOT CHANGE THIS FILE. MAKE A COPY IF YOU WANT TO PLAY.
    
    THE INSTRUCTORS CANNOT GUARANTEE 
    TO PROVIDE SUPPORT ON THE CONTENTS OF THIS FILE.
"""

import time
import pygame

from .pygame_utils import (
    set_up_screen,
    get_event,
    show_message,
    draw_minesweeper_game,
)

from minesweeper_game_project.minesweeper_game.constants import SQUARE_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from minesweeper_game_project.minesweeper_game.mines import MinesweeperGame

def transform_pos_to_grid(pos: tuple) -> tuple:
    return pos[1]//SQUARE_SIZE, pos[0]//SQUARE_SIZE

def main():
    screen = set_up_screen()
    ## Initialize the game according to the screen and square size.
    mines = MinesweeperGame(
        SCREEN_HEIGHT//SQUARE_SIZE,
        SCREEN_WIDTH//SQUARE_SIZE
    )
    draw_minesweeper_game(screen, mines)
    while True:
        event = get_event()
        if event.type == pygame.QUIT:
            break
        if mines.is_running():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x, y = transform_pos_to_grid(pos)
                if event.button == 1:
                    # If player left clicked of the grid
                    mines.click(x, y)
                elif event.button == 3:
                    # If player right clicked of the grid
                    mines.right_click(x, y)
                draw_minesweeper_game(screen, mines)
            time.sleep(0.01)
        elif mines.found_all_mines():
            # If the player has found all the mines, they win
            show_message(screen, "You win!")
        else:
            show_message(screen, 'You lost')


if __name__ == '__main__':
    main()
