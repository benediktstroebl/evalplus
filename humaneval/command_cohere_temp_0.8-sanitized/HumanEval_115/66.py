import math
def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.
    """
    # Make sure the input is a list of lists and remove extra lines at the end of each well.
    grid = [line for line in grid if line != []]

    if not grid:
        return 0

    # Calculate the dimensions of the grid
    N, M = len(grid), len(grid[0])
    result = 0

    # Define a recursive helper function
    def dfs(row, col, current_capacity):
        if col >= M or row >= N:
            return current_capacity
        if grid[row][col] == 0:
            return dfs(row + 1, col, current_capacity)
        elif current_capacity >= capacity:
            result += 1
            return dfs(row, col + 1, current_capacity - capacity)
        else:
            return dfs(row, col + 1, current_capacity)

    # Start the recursive function at the top-left corner with a full bucket
    return result + dfs(0, 0, capacity)
capacity = 1