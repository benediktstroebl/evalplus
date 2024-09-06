
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
    # pass
    # solution by: Mohamed Abouelenein
    # linear solution O(mn)
    # m: number of rows
    # n: max number of cols in a row
    
    # data: a 2 dimensional data, as a nested lists
    # x: integer
    # return: list of tuples, [(x1, y1), (x2, y2) ...] such that
    # each tuple is a coordinate - (row, columns), starting with 0.
    
    # find coordinates of all x
    coordinates = []
    
    # loop over all rows
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == x:
                coordinates.append((i, len(row) - 1 - j))
    # sort by rows in ascending order
    coordinates = sorted(coordinates, key=lambda x: x[0])
    # sort by columns in descending order
    coordinates = sorted(coordinates, key=lambda x: x[1], reverse=True)
    
    return coordinates
    
    
    # # solution by: admin
    # # linear solution O(mn)
    # # m: number of rows
    # # n: max number of cols in a row
    
    # # data: a 2 dimensional data, as a nested lists
    # # x: integer
    # # return: list of tuples, [(x1, y1), (x2, y2) ...] such that
    # # each tuple is a coordinate - (row, columns), starting with 0.
    
    # # find coordinates of all x
    # coordinates = []
    
    # # loop over all rows
    # for i, row in enumerate(data):
    #     for j, val in enumerate(row):
    #         if val == x:
    #             coordinates.append((i, j))
    
    # # sort by rows in ascending order
    # coordinates = sorted(coordinates, key=lambda x: x[0])
    
    # # loop over all rows
    # for i, row in enumerate(data):
    #     for j, val in enumerate(row):
    
