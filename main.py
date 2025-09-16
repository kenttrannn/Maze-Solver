#Kent Tran, Matthew Trinh
#September 16, 2025
#Maze Game

import check_input

def read_maze():
    """
    Reads the maze from the file and store the contents in a 2D list.
    Args: none
    Returns: maze
    Raises: 
    """
    maze = []
    with open("maze.txt", "r") as file:
        for line in file:
            row = list(line.rstrip('\n'))
            maze.append(row)
        return maze

def find_start(maze):
    """
    Finds the starting point of the maze
    Args: Maze
    Returns: Starting point 's'
    Raises:
    """
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 's':
                return [row, col]

def display_maze(maze, loc):
    """
    Displays the maze with the player's current location as 'X'
    Args: Maze, Location
    Returns: Maze with player's location
    Raises:
    """
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if row == loc[0] and col == loc[1]:
                print('X', end='')
            else:
                print(maze[row][col], end='')
        print()

def main():
    """Handles main game loop"""
    print("-Maze Solver-")
    
    maze = read_maze()
    if maze is None:
        print("Error: Could not read maze from file.")
        return

    user_location = find_start(maze)
    if user_location is None:
        print("Error: Could not find starting point in maze.")
        return

    while True:
        display_maze(maze, user_location)

        current_location = maze[user_location[0]][user_location[1]]
        if current_location == 'f':
            print("Congratulations! You found the end of the maze!")
            break
      
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
      
        user_input = check_input.get_int_range("Enter choice: ", 1, 4)

        new_row = user_location[0]
        new_col = user_location[1]
      
        if user_input == 1:
            new_row -= 1
        elif user_input == 2:
            new_row += 1
        elif user_input == 3:
            new_col += 1
        elif user_input == 4:
            new_col -= 1

        if (new_row >= 0 and new_row < len(maze) and
            new_col >= 0 and new_col < len(maze[new_row]) and
            maze[new_row][new_col] != '*'):
            user_location[0] = new_row
            user_location[1] = new_col
        else:
            print("You cannot move there.")
        
main()