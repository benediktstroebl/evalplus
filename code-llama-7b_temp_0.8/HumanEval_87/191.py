
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
    # [
    #   [1,2,3,4,5,6],
    #   [1,2,3,4,1,6],
    #   [1,2,3,4,5,1]
    # ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    # get_row([], 1) == []
    # get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]

    #if the list is empty, return empty list
    if lst == []:
        return []

    #make the lst a dictionary, where keys are index of rows
    #and the values are the rows
    lst_dict = {}
    for i in range(len(lst)):
        lst_dict[i] = lst[i]

    #define a function that, given a coordinate (row, column),
    #returns a tuple (row, column, x).
    #if x is the element of the row (it's value),
    #return a tuple (row, column, x).
    #otherwise, return a tuple (row, column, 0).
    def get_val(row, column):
        if lst[row][column] == x:
            return (row, column, x)
        else:
            return (row, column, 0)

    #define a function that, given a coordinate (row, column),
    #returns a tuple (row, column, x).
    #if x is the element of the row (it's value),
    #return a tuple (row, column, x).
    #otherwise, return a tuple (row, column, 0).
    def get_val(row, column):
        if lst[row][column] == x:
            return (row, column, x)
        else:
            return (row, column, 0)

    #make an empty list for tuples
    lst_tuples = []

    #add tuples to the list, where each tuple is a coordinate
    #in the list starting with 0
