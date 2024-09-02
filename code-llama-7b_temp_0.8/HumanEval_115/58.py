
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
    # The solution is to use bfs with a queue for each column
    # this gives you the maximum number of times that the 
    # heights can be changed
    # If we want to find the minimum number of changes, we can use
    # a similar approach but make use of a max heap.
    # We can do this by using heapq.heapify to convert our array into
    # a heap and then updating the heap with the max value at each 
    # iteration.

    # 1. Get the grid size
    # 2. Get the initial heights
    # 3. Create the initial buckets
    # 4. Loop through each row and column using a queue
    # 5. When the row is empty, dequeue and update
    # 6. Once all rows have been emptied, return the count

    heights = [row[::-1] for row in grid]
    row_count, col_count = len(heights), len(heights[0])

    def make_buckets():
        return [0] * col_count

    def change_height(i, j, change):
        heights[i][j] += change

    def can_change(i, j):
        return heights[i][j] >= 1

    def change_bucket(col, change):
        buckets[col] += change

    def get_max_bucket_height():
        return max(buckets)

    def get_bucket_height(col):
        return buckets[col]

    def can_fill_bucket(col):
        return buckets[col] < capacity

    def get_heights(i, j):
        return heights[i][j]

    buckets = make_buckets()
    count = 0
    change_height(0, 0, -1)
    for i in range(row_count):
        col_q = []
        for j in range(col_count):
            if heights[i][j] > 0:
                col_q.append(j)

        while len(col_q) > 0:
            col = col_q
