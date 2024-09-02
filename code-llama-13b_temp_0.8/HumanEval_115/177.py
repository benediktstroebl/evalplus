
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
    # kullanıcıdan girdiler alındı.
    # grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    # capacity = 1
    # 4 x 4 matris
    # kullanıcıdan alınan grid matrisinin satırlarının uzunluğunu kullanıcıya sor.
    row_length = int(input("Enter the length of rows: "))
    # kullanıcıdan alınan grid matrisinin sütünlarının uzunluğunu kullanıcıya sor.
    col_length = int(input("Enter the length of columns: "))
    grid = []
    # 4 x 4 matris oluştur.
    # örnek olarak 2 x 2 için: [[0, 0], [0, 0]]
    for i in range(row_length):
        temp = []
        for j in range(col_length):
            temp.append(0)
        grid.append(temp)
    # örnek olarak 2 x 2 için: [[1, 1], [1, 0]]
    for i in range(row_length):
        for j in range(col_length):
            print("Please enter value for grid[" + str(i) + "][" + str(j) + "]: ", end="")
            grid[i][j] = int(input())

    # O(N^2)
    # * 4 x 4 matris için
    # * kenarlıklarda 0
    # * diagonal hariç diğer elemanlarında 1
    # 
    # 0 0 1 0
    # 0 1 0 0
    # 1 1 1 1
    for i in range(row_length):
        # 4 x 4 matris için
        # 1. satır 1 elemanından itibaren 1
