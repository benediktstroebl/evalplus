
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
    # Step 1: Sorting the coordinates in ascending order of rows
    coords = sorted(lst, key=lambda x: x[0])
    
    # Step 2: Creating empty list for return value
    return_list = []
    
    # Step 3: Traversing the sorted coordinates
    for i in range(0, len(coords)):
        coord = coords[i]
        x = coord[0]
        for j in range(1, len(coord)):
            y = coord[j]
            return_list.append((x, y))
            x += 1
    
    return return_list