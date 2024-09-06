
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
    # Check for k > N * N
    if k > len(grid) * len(grid[0]):
        raise ValueError("K cannot be larger than N * N")

    # Find max x,y for the grid
    x_max = len(grid[0]) - 1
    y_max = len(grid) - 1

    # Find the starting point
    start = find_starting_point(grid, x_max, y_max)

    # Start on the grid[start[0]][start[1]]
    x = start[0]
    y = start[1]

    # Set up the result list
    result = list()

    # Set up the directions
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Loop through the grid k times
    while k > 0:

        # Append the value at x,y to the result list
        result.append(grid[y][x])

        # Decrement k
        k -= 1

        # Find the nearest k, if any
        # start by initializing min_dist
        min_dist = len(grid) + len(grid[0])

        # Loop through the directions
        for dir in directions:

            # Set up the next direction
            next_x = x + dir[0]
            next_y = y + dir[1]

            # If the next_x is in range, and next_y is in range
            if in_range(next_x, next_y, x_max, y_max):
                # Calculate the distance to the next x,y
                dist = grid[next_y][next_x]

                # If the distance is less than the min_dist
                if dist < min_dist:
                    # Set min_dist to dist
                    min_dist = dist

        # Set the new x,y
        x += directions[grid[y][x] - 1][0]
        y += directions[grid[y][x] - 1][1]

    # Return the result
    return result
