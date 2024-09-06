
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
    #Makes sure that k is greater or equal to 1
    if k < 1:
        k = 1

    #initializes a list to store the minimum path
    minimum_path = []

    #iterates over the grid
    for i in range(len(grid)):
        #iterates over the columns of the grid
        for j in range(len(grid[i])):
            #checks if the path length is the same as the k
            if k == 1:
                #sets the minimum path as the current cell
                minimum_path = grid[i][j]
                break
            else:
                #sets a variable that will be used to check if the
                #minimum path is smaller than the current path
                is_smaller_path = False

                #creates a copy of the grid
                new_grid = []
                for line in grid:
                    new_grid.append(line.copy())

                #iterates over the possible paths
                for path in [[i-1,j],[i,j-1]]:
                    #checks if it is a valid path
                    if path[0] >= 0 and path[1] >= 0:
                        #sets the new grid as the current grid
                        new_grid[i][j] = grid[i][j]
                        #sets the current cell as the cell that the
                        #current path goes to
                        new_grid[path[0]][path[1]] = grid[i][j]
                        #decrements the path length
                        k -= 1
                        #calls the recursive function
                        minimum_path_aux = minPath(new_grid, k)
                        #checks if the current path is smaller than the
                        #minimum path
                        if minimum_path_aux < minimum_path:
                            #sets the minimum path as the current path
                            minimum_path = minimum_path_aux
                            #sets a variable to True
                            is_smaller_path = True
                        #resets the grid
                        new_grid = []
                        for line in grid:
                            new_grid.append(line
