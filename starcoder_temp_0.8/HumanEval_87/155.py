
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
    # list to store the coordinates of the integers
    result = []

    # check if the list is empty
    if not lst:
        return result

    # loop through the list
    for row, val in enumerate(lst):
        # loop through each value in the row
        for col, val2 in enumerate(val):
            # check if the value is equal to the given integer
            if val2 == x:
                # store the coordinate (row, column) in the result list
                result.append((row, col))

    # sort the list by rows
    result.sort()

    # sort the list by columns
    for i in range(len(result) - 1):
        for j in range(i + 1, len(result)):
            if result[i][1] < result[j][1]:
                result[i], result[j] = result[j], result[i]

    return result
