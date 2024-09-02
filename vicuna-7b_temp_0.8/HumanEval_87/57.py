
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
    lst = lst[0]  # Get the first row
    row = [x for x in lst]  # Get all elements in the first row
    row.sort(key=lambda x: cnt(x))  # Sort rows first by number of elements
    for i in range(len(row)):
        row[i] = [cnt(x) for x in row[i]]  # Sort elements of each row by number of elements
        cnt(row[i][j]) += 1  # Keep track of number of elements in each row
    return row
