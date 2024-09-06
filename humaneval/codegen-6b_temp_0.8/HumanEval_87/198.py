
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
    result = []
    
    def insert(x):
        if not result or result[-1][0] != x[0]:
            result.append((x[0], len(result) if result else 0))
        return result[-1][1]
    
    if lst:
        row_of_first_element = lst[0][0]
        column_of_first_element = lst[0][1]
        
        for row_number in range(len(lst)):
            lst[row_number].sort(key=lambda x: (-x[1], x[0]))
            for index in range(len(lst[row_number])):
                lst[row_number][index] = (lst[row_number][index][1], insert(lst[row_number][index][0]))
        
        for row_number in range(len(lst)):
            lst[row_number].sort(key=lambda x: (-x[0], x[1]))
            for index in range(len(lst[row_number])):
                lst[row_number][index] = (lst[row_number][index][1], insert(lst[row_number][index][0]))
        
        lst.sort(key=lambda x: (-x[0][0], x[0][1]))
        for row in lst:
            for i in range(len(row)):
                row[i] = (row[i][1], row[i][0])
        
        for row in lst:
            for index in range(len(row)):
                row[index] = (row[index][1], row[index][0])
        
        for row in range(len(lst)):
            for index in range(len(lst[row])):
                lst[row][index] = lst[row][index][0]
        
        for row in range(len(lst)):
            for index in range(len(lst[row])):
                lst[row][index] = lst[row][index][1]
    
    return map