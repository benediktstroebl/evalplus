
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
    rows, cols = len(grid), len(grid[0])
    totals = [] 
    for i in range(rows):
        total = 0
        for j in range(cols):
            total += grid[i][j]
            totals.append(total)
    
    def get_total(i, total):
        if i == rows:
            return total
        total += totals[i]
        return get_total(i + 1, total)

    # time complexity = O(n * (n + 1) / 2)
    # space complexity = 2n
    def dfs(i, j, total):
        if i == rows:
            return 0
        total = max(total, grid[i][j])
        return min(total, grid[i][j]) + dfs(i + 1, j, total)

    # time complexity = O(n * (n + 1) / 2)
    # space complexity = 2n
    def bfs(i, j, total):
        queue = [(i, j, total)]
        while queue:
            i, j, total = queue.pop(0)
            if i == rows:
                return 0
            total = max(total, grid[i][j])
            queue.append((i, j + 1, total))
            # queue.append((i, j - 1, total))
            queue.append((i + 1, j, total))
            # queue.append((i - 1, j, total))
        return total
    
    # final_value = get_total(0, 0)
    # if final_value < capacity:
    #     print(0)
    # else:
    #     print(final_value - capacity)
    # return final_value - capacity

    return bfs(0, 0, 0) - capacity
