
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
    # your code here
    result = []
    
    # If the list is empty, return empty list
    if lst == []:
        return result
    
    # Iterate through the list
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    
    # Sort the result by rows in ascending order
    result.sort(key=lambda x: x[0])
    
    # Sort the result of the same row by columns in descending order
    for i in range(len(lst)):
        for j in range(len(lst)):
            if result[i][0] == result[j][0]:
                if result[i][1] < result[j][1]:
                    result[i], result[j] = result[j], result[i]
    
    return result
