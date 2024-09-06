
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
    # TODO: figure out the O(n^2) solution first, and then translate to
    # O(nlogn) with a heap.
    import heapq

    # Assumes that each well has the same number of units of water.
    # So we can just flatten the grid and do a sorting operation.
    # This will also remove the 1's from the grid and put them
    # in a list.

    heap = []
    for row in grid:
        heapq.heappush(heap, -1 * sum(row))

    # Now, we can process the buckets.
    # If the top element is less than the capacity, we can
    # take all of the top element.
    # If it is greater than the capacity, we can take the capacity
    # of the top element, and then add another bucket back on the
    # heap for the remaining elements.

    n_buckets = 0
    current_capacity = 0

    while heap:
        # TODO: implement this.
        # print(heap)
        min_fill = heap[0]
        current_capacity += min_fill
        heapq.heappop(heap)

        if current_capacity >= capacity:
            current_capacity = 0
            n_buckets += 1

    return n_buckets
