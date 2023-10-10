import arcade
import time;

def main(): 
    window = arcade.open_window(800, 600, 'dsflk')
    window.background_color = arcade.csscolor.SKY_BLUE

    arcade.start_render()
    # arcade.draw_lrtb_rectangle_filled(0, 800, 300, 0, arcade.csscolor.GREEN)
    arcade.draw_xywh_rectangle_filled(0, 0, 800, 300, arcade.csscolor.AZURE)
    arcade.finish_render()
    arcade.run()


main()