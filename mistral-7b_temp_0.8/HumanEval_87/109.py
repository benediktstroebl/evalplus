
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
    # Initialize the output list.
    result = []

    # Iterate through the row.
    for row in lst:
        # Find the number of columns in the row.
        cols = len(row)

        # Iterate through the columns.
        for col in range(cols):
            # Check if the value in the row at the column is equal to the value given.
            if row[col] == x:
                # Add the tuple to the result list.
                result.append((row.index(row[col]), col))

    # Sort the result list by the row, in ascending order, and then by the column, in descending order.
    result.sort(key=lambda t: (t[0], -t[1]))

    # Return the result list.
    return result

