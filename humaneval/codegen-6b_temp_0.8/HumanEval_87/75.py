
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
    
    # initializing a sorted list
    sorted_list = sorted(lst, key = lambda row: row[0], reverse=True)
    
    # initialize a list to hold coordinates and the initial sorting order
    coordinates = []
    
    # loop through the sorted list of rows
    for row in sorted_list:
        
        # if the row is not empty
        if row != []:
            
            # loop through the list of columns
            for col in sorted(row, reverse=True):
                
                if col == x:
                    
                    # append a tuple of (col, row)
                    coordinates.append((row.index(col), row.index(col)))
                    
    return coordinates
