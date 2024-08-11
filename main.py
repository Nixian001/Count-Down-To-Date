import pygame
import datetime
import os

# Initialize Pygame
pygame.init()

# Set the end time for the countdown
# YYYY, MM, DD, HH, mm, SS, Tz
end_time = datetime.datetime(2024, 10, 22, 0, 0, 0, 0)

# Set up the screen, font, and clock
screen = pygame.display.set_mode((1100, 200))
font = pygame.font.SysFont('Arial', 30)
clock = pygame.time.Clock()


def countdown(stop_time):
    running = True
    while running:
        # Handle Pygame events (e.g., allowing the window to close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Calculate the time difference
        now = datetime.datetime.now()
        difference = stop_time - now

        # Extract hours, minutes, and seconds from the difference
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)

        # Check if the countdown has finished
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            print("Goodbye!")
            running = False

        # Format the countdown text
        countdown_text = (
            f'Date is in: {difference.days} day(s) '
            f'{count_hours} hour(s) {count_minutes} minute(s) '
            f'{count_seconds} second(s)'
        )

        # Print the countdown in the console
        # print(countdown_text)

        # Render the text
        text_surface = font.render(countdown_text, True, (101, 184, 94))

        # Get the rectangle of the text surface and center it
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

        # Update the display with the centered countdown
        screen.fill((0, 0, 0))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        clock.tick(60)


# Start the countdown
countdown(end_time)
