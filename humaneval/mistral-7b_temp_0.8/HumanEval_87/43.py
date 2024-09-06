
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

    # First sort the list in ascending order, so that
    # if there are two rows that have same x, we can take the first row.
    lst.sort(key=lambda x: x[0])

    # Next, we take the x coordinate of each row, and
    # sort them in descending order
    x_lst = []
    for row in lst:
        for element in row:
            if element == x:
                x_lst.append((row.index(element), row))

    # Now we sort the x_lst by row in ascending order.
    x_lst.sort(key=lambda x: x[0][0])

    # And, finally, we sort the x_lst by column in descending order
    x_lst.sort(key=lambda x: x[0][1], reverse=True)

    # For each row in x_lst, we get the coordinates of the row.
    x_lst_new = []
    for element in x_lst:
        x_lst_new.append((element[0][0], element
