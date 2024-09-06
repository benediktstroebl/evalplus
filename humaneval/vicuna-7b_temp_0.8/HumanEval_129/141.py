
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
    if not grid:
        return []

    # create a priority queue to keep track of the paths
    pq = [(0, grid)]
    visited = set()
    while pq:
        # get the path with the minimum sum from the priority queue
        path = pq.pop(0)
        total_sum = sum(path)
        if total_sum == k:
            # if the path has the correct length, return its values
            return list(path)
        for cell in path:
            # mark the cell as visited
            visited.add(cell)
        # add the current path to the priority queue with the updated sum
        for i in range(total_sum - k + 1):
            for j in range(len(path)):
                # calculate the new path
                new_path = []
                for i in path:
                    if i not in visited:
                        new_path.append(i)
                    else:
                        break
                if new_path:
                    # add the new path to the priority queue
                    path_len = sum(new_path)
                    path_values = list(new_path)
                    pq.append((path_len, path_values))

    # if no path is found, return an empty list
    return []