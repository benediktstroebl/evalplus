
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
    # some type checking first
    if not lst or not isinstance(lst, list):
        return []
    if not lst[0] or not isinstance(lst[0], list):
        return []
    if not isinstance(x, int):
        return []

    # index the row
    rows = {}
    for index, row in enumerate(lst):
        # first count the row
        row_length = 0
        # we only care about rows that contain our x
        if x in row:
            # track the index of where x appears
            rows[index] = []
            # now go over the row and track the index of x
            for index2, col in enumerate(row):
                if col == x:
                    rows[index].append(index2)
                    row_length += 1
            # sort the index
            rows[index].sort()
            rows[index].reverse()

    # now we need to sort the rows, and if a row is empty, remove it
    final_list = []
    for index, row in sorted(rows.items()):
        # if the row is empty, skip it
        if not row:
            continue
        # if it's not empty, add it to the final list
        for i in row:
            final_list.append((index, i))

    # return the list
    return final_list

