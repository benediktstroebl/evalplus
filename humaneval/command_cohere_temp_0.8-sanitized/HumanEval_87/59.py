def get_row(matrix, x):
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

    def sort_key(coord):
        row_idx, col_idx = coord
        return (-col_idx, row_idx)

    result = []
    row_num = row_idx = 0
    for row in matrix:
        col_idx = 0
        for val in row:
            if val == x:
                result.append((row_idx, col_idx))
                break
            col_idx += 1
        row_idx += 1
    result.sort(key=sort_key)
    return result
x = 1