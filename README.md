# Conway's Game of Life Simulation

![image](https://github.com/koopa35/CGL/assets/87890771/00301d16-d870-4434-aa87-73fdcecb0cf4)

This code simulates Conway's Game of Life using the Pygame library. The Game of Life is a cellular automaton that follows simple rules to evolve a population of cells on a two-dimensional grid.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone this repository to your local machine:
   ```
   git clone [repository URL]
   ```

2. Navigate to the project directory:
   ```
   cd [repository name]
   ```

3. Install the required dependencies:
   ```
   pip install pygame
   ```

## Usage

1. Adjust the user inputs at the beginning of the code to customize the simulation:
   - `RES`: Screen resolution (width, height) in pixels.
   - `FPS`: Frames per second for the simulation.
   - `SIZE`: Pixel size for representing alive cells on the grid.
   - `DENSITY`: Controls the density of initial alive cells. A higher value means less dense population.

2. Run the code:
   ```
   python cgl.py
   ```

3. In the Pygame window, you will see a grid of cells. The alive cells are represented by white rectangles.

4. Press the 'W' key to evolve the population according to the rules of Conway's Game of Life. The new state of each cell is determined by its neighbors.

5. To exit the simulation, close the Pygame window or press the 'X' button.

## Contributing

Contributions to the project are welcome. If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

Code written by Connor Powell
