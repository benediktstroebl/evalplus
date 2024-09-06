
def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    # Check if there is no valid path
    if not grid:
        return []
    
    if not grid:
        return []
    
    # Create an empty list to store the minimum path
    min_path = []
    
    for i in range(1, len(grid)):
        # Create a list to store the current path
        path = [grid[i][0]]
        path_len = 1
        
        while len(path) < k:
            # If the path is not full
            if path_len < k:
                # Get the current cell at index i of the grid
                current_cell = grid[i][0]
                
                # Find the next cell to go to
                next_cell = None
                next_x = i - current_cell
                next_x = next_x // 2
                next_x = next_x - (next_x % 2)
                
                if -2 <= next_x <= 2:
                    next_cell = grid[next_x][0]
                else:
                    next_cell = None
                    
                # If the next cell is valid
                if next_cell:
                    # If the next cell is not already in the path
                    if next_cell not in path:
                        # Add the next cell to the path and update the path length
                        path.append(next_cell)
                        path_len += 1
                        
                        # If the path is not full
                        if path_len < k:
                            # Find the next cell to go to
                            next_cell = None
                            next_y = i - next_cell
                            next_y = next_y // 2
                            next_y = next_y - (next_y % 2)
                            
                            if -2 <= next_y <= 2:
                                next_cell = grid[next_y][0]
                            else:
                                next_cell = None
                        
                # If the next cell is not valid
                else:
                    path = path[:-1]
                    path_len = path_len - 1
    
    # Add the
