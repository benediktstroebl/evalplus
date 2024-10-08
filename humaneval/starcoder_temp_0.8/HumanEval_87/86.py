
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
    result = []
    # for every row in the list
    for i in range(len(lst)):
        # if the row contains the value x
        if x in lst[i]:
            # for every column in the row
            for j in range(len(lst[i])):
                # if the value in the column is equal to x
                if lst[i][j] == x:
                    # add to the result list the coordinate (i, j)
                    result.append((i, j))
    # return sorted result
    return sorted(sorted(result, key = lambda coordinate : coordinate[0]), key = lambda coordinate : coordinate[1], reverse=True)
