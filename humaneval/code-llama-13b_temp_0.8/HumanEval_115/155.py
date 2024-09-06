
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
    # # Main Idea
    # # 1. Split the grid into horizontal, vertical and diagonal lines
    # # 2. Split the vertical lines into the smallest possible sections
    # # 3. Split the lines into buckets
    # # 4. Sum up the number of buckets needed
    # 
    # # Split into horizontal, vertical and diagonal lines
    # # horizontal_lines, vertical_lines, diagonal_lines = [], [], []
    # # for row in grid:
    # #     horizontal_lines.append(row)
    # #     diagonal_lines.append(row)
    # #     vertical_lines.append([x for x in row])
    # # 
    # # # Split into the smallest possible sections
    # # for i, line in enumerate(horizontal_lines):
    # #     for j, cell in enumerate(line):
    # #         if cell == 1:
    # #             horizontal_lines[i][j:j+cell] = [1 for x in range(cell)]
    # # 
    # # for i, line in enumerate(vertical_lines):
    # #     for j, cell in enumerate(line):
    # #         if cell == 1:
    # #             vertical_lines[i][j:j+cell] = [1 for x in range(cell)]
    # # 
    # # # Split into buckets
    # # number_of_buckets = 0
    # # for line in vertical_lines:
    # #     for i in range(0, len(line), capacity):
    # #         line[i:i+capacity] = [capacity for x in range(len(line[i:i+capacity]))]
    # #         number_of_buckets += 1
    # # 
    # # for line in horizontal_lines:
    # #     for i in range(0, len(line), capacity):
    # #         line[i:i+capacity] = [capacity for x in range(len(line[i:i+capacity]))]
    # #         number_of_buckets += 1
    # # 
    # # for i in range(0
