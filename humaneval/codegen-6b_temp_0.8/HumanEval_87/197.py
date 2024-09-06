
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
    if not lst or not lst[0]:
        return []
    
    def sort_coord(coord):
        (row, col) = coord
        return (row, -col)
        
    row_to_coord = sorted([(i, lst[i].index(x)) 
                                for i in range(len(lst))], key=sort_coord)
    
    return [tuple(row_to_coord[i][:2]) 
        for i in range(len(row_to_coord))]

assert get_row([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
assert get_row([], 1) == []
assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
assert get_row([[1,2,3], [4,3,2], [1,2,3]], 2) == [(1,2),(2,1),(1,2)]
assert get_row([[1,1,1,1,1,1], [2,3,4,5,6,7], [8,9,10,11,12,13], [14,15,16,17,18,19]], 1) == [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (1,4), (2,0), (2,1), (2,2), (2,3), (2,4), (3,0), (3,1), (3,2), (3,3), (3,4), (4,0), (4,1), (4,2), (4,3), (4,4)]
assert get_row([[1,2,3], [4,3,2], [1,2,3]], 2) == [(1