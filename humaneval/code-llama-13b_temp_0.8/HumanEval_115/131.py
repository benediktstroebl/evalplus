
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
    def get_index(row, col):
        return row * grid.shape[1] + col

    def get_row_col(index):
        row = int(index / grid.shape[1])
        col = index % grid.shape[1]
        return (row, col)

    # find number of cells and neighbours
    n_cells = grid.shape[0] * grid.shape[1]
    n_neighbours = grid.shape[0] + grid.shape[1] + 2

    # find distances from every node to every other node
    d_matrix = np.full((n_cells, n_cells), np.inf)
    for i in range(n_cells):
        row, col = get_row_col(i)
        for j in range(i+1, n_cells):
            row_j, col_j = get_row_col(j)
            d_matrix[i, j] = d_matrix[j, i] = math.sqrt((row - row_j)**2 + (col - col_j)**2)
    for i in range(n_cells):
        d_matrix[i, i] = 0

    # for every cell in a row, find the closest other cell in the row
    row_closest_cell = np.full((grid.shape[0], grid.shape[1]), np.inf)
    for i in range(grid.shape[0]):
        row_closest_cell[i, :] = np.min(d_matrix[get_index(i, 0): get_index(i+1, 0)], axis=0)

    # for every cell in a column, find the closest other cell in the column
    col_closest_cell = np.full((grid.shape[0], grid.shape[1]), np.inf)
    for i in range(grid.shape[1]):
        col_closest_cell[:, i] = np.min(d_matrix[get_index(0, i): get_index(grid.shape[0], i)], axis=0)

    # find
