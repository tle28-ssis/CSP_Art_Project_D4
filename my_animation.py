import simple_animation as sa

def draw_frame(frame_number, elapsed_seconds, width, height):
    """Draws one frame of an animation. Called approx 60 times per second."""
    
    # I. Background
    # a) Sky
    sa.fill_background("#9cc6e6")

    # b) Cloud
    sa.set_fill_color("white")
    sa.draw_cloud(200, 150, 60)
    sa.draw_cloud(550, 80, 100)

    # c) Hill
    sa.set_fill_color("white")
    sa.set_outline_color("white")
    sa.fill_triangle(0, 300, 1200, 600, 0, 600)

    # d) Trees
    sa.set_outline_color("#257333")
    sa.draw_pine_tree(-80, 350, 200, "#257333")
    sa.draw_pine_tree(0, 400, 200, "#257333")
    sa.draw_pine_tree(100, 450, 200, "#257333")
    sa.draw_pine_tree(200, 450, 200, "#257333")
    sa.draw_pine_tree(300, 480, 200, "#257333")
    sa.draw_pine_tree(400, 520, 200, "#257333")
    sa.draw_pine_tree(500, 560, 200, "#257333")
    sa.draw_pine_tree(-50, 450, 200, "#257333")
    
    # Draw the information text
    sa.set_fill_color("black")
    sa.draw_text(40, 50, f"Frame number: {frame_number}")
    sa.draw_text(40, 80, f"Elapsed Time: {elapsed_seconds:.1f} seconds")
    sa.draw_text(40, 110, f"Mouse x: {sa.get_mouse_x()}")
    sa.draw_text(40, 140, f"Mouse y: {sa.get_mouse_y()}")

    # Draw skier
    new_y = sa.loop_frames(250, 500, 250, frame_number)
    new_x = sa.loop_frames(100, 900, 250, frame_number)
    sa.draw_skier(new_x, new_y, 40)
    
if __name__ == "__main__":
    # Launch the wrapper and tell it to use our draw_frame function
    sa.start(draw_frame)
    

