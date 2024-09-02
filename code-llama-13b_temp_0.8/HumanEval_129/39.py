
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
    #
    # 1. Find the number of sequences
    # 2. Find the first sequence
    # 3. Find the next sequence
    # 4. Find the next sequence (using the prev sequence)
    #
    N = len(grid)
    if N <= 1:
        return grid[0]

    n = N * N
    sqNums = [0] * n

    # Find the number of sequences
    #
    # Use a queue to find the squares
    #
    queue = [0]
    visited = [False] * n
    for i in range(1, N+1):
        for j in range(1, N+1):
            num = i * N + j
            sqNums[num] = 1
            visited[num] = True

            prev = num - 1
            if prev >= 0 and prev % N != N - 1:
                if not visited[prev]:
                    queue.append(prev)
                    visited[prev] = True

            prev = num - N
            if prev >= 0:
                if not visited[prev]:
                    queue.append(prev)
                    visited[prev] = True

    # Find the first sequence
    #
    start = queue[0]
    while True:
        num = start + 1
        if num % N != 0 and not visited[num]:
            sqNums[num] = sqNums[start] + 1
            start = num
            visited[num] = True
        else:
            break

    # Find the next sequence
    #
    # Use a queue to find the next sequence
    #
    queue.clear()
    for i in range(1, N+1):
        for j in range(1, N+1):
            num = i * N + j
            if num != start and num != start + 1:
                queue.append(num)
                visited[num] = True

    for _ in range(1, n):
        # Find the next sequence (using the prev sequence)
        #
        for num in queue:
            prev = num - 1
            if prev >=
