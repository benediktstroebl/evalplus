
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
    def get_index(row, col):
        return len(row) - row[::-1].index(col) - 1

    def row_sorter(coordinates):
        return sorted(coordinates, key=lambda x: x[0])
    
    def col_sorter(coordinates):
        return sorted(coordinates, key=lambda x: (-x[1], x[0]))
    
    coordinates = []
    for row_index, row in enumerate(lst):
        try:
            col_index = row.index(x)
        except ValueError:
            continue
        coordinates.append((row_index, col_index))
    coordinates = row_sorter(coordinates)
    for coordinate in coordinates:
        coordinate[1] = get_index(lst[coordinate[0]], coordinate[1])
    return col_sorter(coordinates)
