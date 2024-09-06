
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
    return

    def get_row(lst, x):
        if len(lst) == 0:
            return []

        rows = []
        for i in range(len(lst)):
            if x in lst[i]:
                rows.append((i, lst[i].index(x)))

        return rows


    # IMPORTANT:
    # Write your solution below
    # We are looking for all rows which contain the number x
    # We can get the row number by looking at the index of the list
    # We can get the column number by looking at the index of the number in the list
    # The output of this function is a list of tuples containing (row, column) coordinates
    # The first item in each tuple is the row, and the second item in each tuple is the column
    # We want to return the list of tuples sorted first by row, and then by column

    # In Python, we can use the .sort() method to sort a list of tuples
    # We can use the lambda function to specify the sorting criteria
    # We can use the .
