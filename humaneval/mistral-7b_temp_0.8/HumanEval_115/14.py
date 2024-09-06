
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
    from queue import PriorityQueue
    row_size = len(grid)
    col_size = len(grid[0])

    # 초기화
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    distance = [[float('inf') for _ in range(col_size)] for _ in range(row_size)]
    for i in range(row_size):
        distance[i][0] = 0
    priority_queue = PriorityQueue()
    # 연결이 되어 있는 위치들 우선순위큐에 넣기
    for i in range(row_size):
        for j in range(col_size):
            if grid[i][j] == 1:
                priority_queue.put((distance[i][j], (i, j)))
    # bfs
    while not priority_queue.empty():
        (d, (r, c)) = priority_queue.get()
        if visited[r][c]: continue
        visited[r][c] = True
