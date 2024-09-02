
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
    n = len(lst)
    if n == 0:
        return []
    
    m = len(lst[0])
    if m == 0:
        return []
    
    def get_row_idx(n, m, row, col):
        return (str(row) + '-' + ('%s' % str(col)), str(row) + '-' + '%s' % str(n-col-1))
    
    # Get the row of the given coordinate,
    # and find the lower and upper number of columns
    lower = 0
    upper = m - 1
    for i in range(n):
        if lst[i][lower] == x:
            row = i
            break
        elif lst[i][upper] == x:
            row = i
            break
    if row == -1:
        return []
    
    # Get the column of the given coordinate
    left = 0
    right = m - 1
    for i in range(m):
        if lst[row][i] == x:
            col = i
            break
        elif lst[row][i] > x:
            right = i - 1
            break
    
    # Get the columns index
    lower = 0
    upper = m - 1
    for i in range(m):
        if lst[row][i] == x:
            left = i
            break
        elif lst[row][i] < x:
            upper = i - 1
            break
    
    # Initialise a list of tuples, [(x1, y1), (x2, y2) ...]
    coordinates = []
    # Iterate through all rows, and append the tuple (row, col)
    for i in range(n):
        coordinate = get_row_idx(n, m, i, col)
        coordinates.append(coordinate)
    
    # Finally, sort the list of tuples, based on column,
    # and return the tuple of coordinates
    coordinates.sort(key=lambda x: (x % 1, x), reverse=True)
    return [tuple(reversed(