
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
    # GRAPH OBJECT
    graph = {}
    # GRAPH'S EDGES
    graph['edges'] = []
    # GRAPH'S NODES
    graph['nodes'] = []

    # GRID DIMENSIONS
    rows = len(grid)
    cols = len(grid[0])

    # FILL UP THE GRAPH OBJECT
    def fill_graph(row, col):
        # if a node is not yet created for the given coordinates
        if not graph['nodes']:
            graph['nodes'].append((row, col))
        # if a node already exists for the given coordinates, skip
        elif (row, col) in graph['nodes']:
            return
        else:
            graph['nodes'].append((row, col))

        # check if the cell underneath is a 1
        if row < rows - 1 and grid[row + 1][col]:
            graph['edges'].append(((row, col), (row + 1, col)))
            fill_graph(row + 1, col)
        
        # check if the cell to the right is a 1
        if col < cols - 1 and grid[row][col + 1]:
            graph['edges'].append(((row, col), (row, col + 1)))
            fill_graph(row, col + 1)

    # GRAPH CONSTRUCTION
    for i in range(rows):
        for j in range(cols):
            fill_graph(i, j)

    # ALIGNED GRID CONSTANTS
    rows = len(graph['nodes'])
    cols = len(graph['edges'])

    # GRAPH OBJECT
    graph_matrix = []

    # GRAPH CONSTRUCTION
    for i in range(rows):
        graph_matrix.append([0] * cols)

    # GRAPH CONSTRUCTION
    for i in range(rows):
        for j in range(cols):
            if (i, j) in graph['edges']:
                graph_matrix[i][j] = 1

    #
