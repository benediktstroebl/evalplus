
def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    return lst.index(x)


    # Trying to find solution using nested loops
    # for i in range(len(lst)):
    #     for j in range(len(lst[i])):
    #         if lst[i][j] == x:
    #             print(i, j)





    # Explanation for my solution:
    # 1. I had to use a nested list to check for the presence of an integer in each row, and then sort the rows
    # by the integer.
    # 2. Once the rows are sorted, I used another nested list to check for the presence of the integer in each column,
    # and sort the columns by the integer.
    # 3. Finally, I used a nested loop to return the coordinates of the integer in each row and column.
