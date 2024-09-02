
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
    
    def bfs(start, grid, visited, start_col, start_row, k, min_path):
        if k == - 1:
            return min_path
        curr_col, curr_row = start_col, start_row
        visited[start_col][start_row] = True
        if start_col == 0 and start_row == 0:
            return bfs((start_col + 1, start_row), grid, visited, start_col, start_row, k - 1, min_path + [start])
        elif start_row == 0:
            return bfs((start_col, start_row + 1), grid, visited, start_col, start_row, k - 1, min_path + [start])
        elif start_col == 0:
            return bfs((start_col + 1, start_row), grid, visited, start_col, start_row, k - 1, min_path + [start])
        else:
            next_steps = []
            left = (curr_col - 1, curr_row)
            right = (curr_col + 1, curr_row)
            up = (curr_col, curr_row - 1)
            down = (curr_col, curr_row + 1)
            if (left[0] < 0) or (left[1] < 0) or (left[0] >= len(grid)) or (left[1] >= len(grid[0])):
                pass
            elif grid[left[0]][left[1]] == None:
                pass
            elif visited[left[0]][left[1]]:
                pass
            elif k == 0:
                next_steps.append(grid[left[0]][left[1]])
            else:
                next_steps.append(grid[left[0]][left[1]])
                bfs(left, grid, visited, left[0], left[1], k - 1, min_path + [str(grid[left[0]][left[1]])])
            if (right[0] < 0) or (right[1] < 0) or (right