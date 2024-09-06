
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
    # Write your code here
    # we can solve this problem using recursion
    # idea is to maximize the total amount of water that we can put in the buckets
    # we use a dp table to find the maximum value that we can put in the buckets
    # but we need to solve the subproblem of finding the maximum value that we can put in the buckets
    # we need to traverse through the 2D matrix
    # we use DFS to solve this problem
    # to solve the subproblem, we need to find the maximum value that we can put in the buckets
    # we can solve this problem by using a recursive solution
    # the base case is when we are at the last row of the matrix
    # we check the maximum value that we can put in the current row
    # we do this by checking the maximum value that we can put in the last column of the matrix
    # and the maximum value that we can put in the row above it
    # we can do this using a recursive function
    # we are calling the recursive function until we get the maximum possible value
    # we are making the assumption that the bucket capacity is 1
    # we need to use the dp solution with the bucket capacity as well
    # if we get a value that is higher than the capacity, then we need to increase the number of operations required
    # we need to add 1 to the number of operations
    # we also need to return the number of operations
    # we should also check if the number of operations is higher than the previous answer
    # we need to return the previous answer
    # we need to make sure that we keep track of the maximum number of operations

    # O(n^2) time | O(n^2) space - where n is the number of rows in the grid
    # we need to do a DFS search on each row
    # we also need to keep track of the maximum value
    def max_fill_rec(grid, capacity, row, col):
        if row == len(grid):
            return grid[row-1][col] if grid[row-1][col] <= capacity else capacity + 1
        left_max = max_fill_rec(grid, capacity, row, col+1)
        upper_max = max_fill_rec(grid, capacity, row+1, col)
        return min(left_max, upper_max) if grid[row][col] == 1 else 0
   
