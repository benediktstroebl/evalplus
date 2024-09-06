
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
    # your code
    # filter the list for x, find the indices of x
    # find the first and last index of x in the row
    # generate the coordinates
    # sort the coordinates by rows first then by columns
    index = [i for i, x in enumerate(lst) if x == x]
    # [(1, 0), (2, 0), (2, 1), (1, 4), (2, 5), (0, 5)]
    ind = []
    for i in index:
        j = i
        while lst[j] == x:
            j += 1
        ind.append((i, j-1))
    ind.sort(key=lambda x: x[0])
    ind.sort(key=lambda x: x[1], reverse=True)
    return ind
