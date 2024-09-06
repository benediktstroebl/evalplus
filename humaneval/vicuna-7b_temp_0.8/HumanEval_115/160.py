
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    # initialize empty list to store visited cells
    visited = [False] * (grid.shape[0] * grid.shape[1])

    # initialize empty list to store the number of times lowering each bucket
    cell_count = [0] * grid.shape[0]

    # loop over each row
    for i in range(grid.shape[0]):
        # loop over each column
        for j in range(grid.shape[1]):
            # check if the cell is already visited
            if visited[i][j]:
                continue

            # if the cell is 1, it means there is water, so add 1 to the count of times lowering this row
            cell_count[i] += 1

            # check if the cell is at the max capacity
            if grid[i][j] == 1 and cell_count[i] >= capacity:
                # if it is, mark it as visited
                visited[i][j] = True

                # loop over all the rows and all the buckets
                for k in range(grid.shape[0]):
                    for p in range(grid.shape[1]):
                        if grid[k][p] == 1:
                            # add the number of times lowering this row to the count of times lowering the bucket
                            count = cell_count[i]
                            cell_count[i] = 0
                            # you don't need to check if the cell is at the max capacity, because the capacity of each bucket is the same
                            bucket_count = max_fill(grid, capacity // cell_count[i])
                            cell_count[i] = count + bucket_count
                            break

    return cell_count[0]