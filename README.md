# Pomodoro Timer

## Description

This project is a simple Pomodoro Timer built using Python's Tkinter library. The Pomodoro Technique is a time management method that encourages focused work sessions followed by short breaks, improving productivity and maintaining mental agility. The timer alternates between work sessions, short breaks, and a longer break after completing multiple work sessions.

The timer's interface is visually appealing, with customizable colors and a display that counts down the time for each session. Users can easily start, stop, and reset the timer, and a checkmark system provides visual feedback on completed work sessions.

**Note**: This project was inspired by Angela Yu's course on Udemy.

## Features

- **Work and Break Sessions**: The timer supports work sessions of customizable duration (default 1 minute) and short (5 minutes) and long (20 minutes) breaks.
- **Visual Countdown**: The timer shows a clear countdown in the format `MM:SS`, with different colors indicating work or break sessions.
- **Session Tracking**: A checkmark system visually tracks completed work sessions, motivating continued productivity.
- **Simple Controls**: Start, stop, and reset the timer with intuitive button controls.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- The Tkinter library (usually included with Python installations).
- A `tomato.png` image file in the same directory as the script (used for the timer's background image).

### How to Use

1. Clone or download the repository to your local machine.
2. Ensure you have the `tomato.png` file in the project directory.
3. Run the script using Python:

   ```bash
   python pomodoro.py
   ```

4. Click the "Start" button to begin the Pomodoro timer.
5. The timer will automatically switch between work sessions and breaks, with the current session displayed at the top.
6. Use the "Reset" button to stop the current session and reset the timer to 00:00.

### Customization

- **Session Durations**: Modify the `WORK_MIN`, `SHORT_BREAK_MIN`, and `LONG_BREAK_MIN` constants to change the length of the work and break sessions.
- **Colors**: Adjust the color constants (`PINK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `COLOR`, `TIMER_COLOR`) to customize the interface's look and feel.
