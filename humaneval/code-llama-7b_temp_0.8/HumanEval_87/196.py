
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
    coords = []
    # getting list of rows
    for i in range(len(lst)):
        if len(lst[i]) != 0:
            coords.append(lst[i])
    # sorting rows
    sorted_rows = sorted(coords)
    # sorting rows' columns
    for i in range(len(sorted_rows)):
        sorted_rows[i] = sorted(sorted_rows[i], reverse=True)

    if sorted_rows != []:
        # getting list of row indices
        row_indices = [i for i in range(len(sorted_rows))]
        # sorting row indices in ascending order
        sorted_row_indices = sorted(row_indices)
        # initializing variables to store the coords
        result = []
        # initializing row index
        row_index = 0
        # initializing columns index
        column_index = 0
        # initializing row index to check
        row_to_check = sorted_rows[row_index][column_index]
        # adding the coordinates to the list
        while row_to_check != x:
            if row_to_check > x:
                row_index -= 1
                if row_index >= 0:
                    row_to_check = sorted_rows[row_index][column_index]
                    column_index += 1
            else:
                row_index += 1
                if row_index < len(sorted_rows):
                    row_to_check = sorted_rows[row_index][column_index]
                    column_index += 1
        result.append([row_index, column_index - 1])
        # getting the next coordinates
        while row_to_check != 1:
            row_to_check = sorted_rows[row_index][column_index]
            # adding the coordinates to the list
            result.append([row_index, column_index - 1])
            # getting the next coordinates
            if row_to_check != x:
                if row_to_check > x:
                    row_index -= 1
                    if row_index >= 0:
                        row
