import random
import simple_animation as sa

# Global list to store snowflake positions: [{'x': x_val, 'y': y_val, 'speed': speed_val, 'radius': r_val}, ...] by Nam M
snowflakes = []

def init_snowflakes(width, height, count=60):
    """Initializes the snowflake positions randomly across the screen."""
    # Written by AI to make the animation smoother
    global snowflakes
    snowflakes = []
    for _ in range(count):
        snowflakes.append({
            'x': random.uniform(0, width),
            'y': random.uniform(0, height),
            'speed': random.uniform(1.0, 2.5),
            'radius': random.uniform(2, 5)
        })
    
def draw_frame(frame_number, elapsed_seconds, width, height):
    """Draws one frame of an animation. Called approx 60 times per second."""
    global snowflakes
    
    # Initialize snowflakes on the very first frame by Nam
    if frame_number == 0 or not snowflakes:
        init_snowflakes(width, height, count=70)
    
    # I. Background by Tea 
    # a) Sky by Tea
    sa.fill_background("#9cc6e6")

    # b) Cloud by Tea
    sa.set_fill_color("white")
    sa.draw_cloud(200, 150, 60)
    sa.draw_cloud(550, 80, 100)

    # c) Hill by Tea
    sa.set_fill_color("white")
    sa.set_outline_color("white")
    sa.fill_triangle(0, 300, 1200, 600, 0, 600)

    # d) Trees by Tea
    sa.set_outline_color("#257333")
    sa.draw_pine_tree(-80, 350, 200, "#257333")
    sa.draw_pine_tree(0, 400, 200, "#257333")
    sa.draw_pine_tree(100, 450, 200, "#257333")
    sa.draw_pine_tree(200, 450, 200, "#257333")
    sa.draw_pine_tree(300, 480, 200, "#257333")
    sa.draw_pine_tree(400, 520, 200, "#257333")
    sa.draw_pine_tree(500, 560, 200, "#257333")
    sa.draw_pine_tree(-50, 450, 200, "#257333")
    
    # Draw the information text by Tea
    sa.set_fill_color("black")
    sa.draw_text(40, 50, f"Frame number: {frame_number}")
    sa.draw_text(40, 80, f"Elapsed Time: {elapsed_seconds:.1f} seconds")
    sa.draw_text(40, 110, f"Mouse x: {sa.get_mouse_x()}")
    sa.draw_text(40, 140, f"Mouse y: {sa.get_mouse_y()}")

    # Draw skier by Joshua
    new_y = sa.loop_frames(250, 500, 250, frame_number)
    new_x = sa.loop_frames(0, 900, 250, frame_number)
    sa.draw_skier(new_x, new_y, 40)
    
    # II. Snowflakes Animation by Nam M
    sa.set_fill_color("white")
    sa.set_outline_color("white")
    
    for flake in snowflakes:
        # Draw the snowflake by Nam M
        sa.fill_circle(flake['x'], flake['y'], flake['radius'])
        
        # Move snowflake down based on its unique speed by Nam M
        flake['y'] += flake['speed']
        
        # Add a subtle drift to the left/right to simulate wind by Nam M
        flake['x'] += random.uniform(-0.3, 0.5) 
        
        # Reset snowflake to the top if it falls off the bottom screen edge by Nam M
        if flake['y'] > height:
            flake['y'] = random.uniform(-10, 0)
            flake['x'] = random.uniform(0, width)
            flake['speed'] = random.uniform(1.0, 2.5)
            
        # Wrap around horizontally if wind pushes it past the side edges by Nam M
        if flake['x'] > width:
            flake['x'] = 0
        elif flake['x'] < 0:
            flake['x'] = width

            
     # Ski lift cable (seobin) 
    base_x = width
    base_y = 230

    peak_x = 0
    peak_y = 0

    sa.set_outline_color("black")
    sa.set_line_thickness(3)
    sa.draw_line(base_x, base_y, peak_x, peak_y)

    # Moving chairs going up-left(Seobin)
    total_frames = 300

    for i in range(5):
        progress = ((frame_number + i * 60) % total_frames) / total_frames

        x = base_x + (peak_x - base_x) * progress
        y = base_y + (peak_y - base_y) * progress

        sa.draw_chair(x, y)



if __name__ == "__main__":
    # Launch the wrapper and tell it to use our draw_frame function
    sa.start(draw_frame)

