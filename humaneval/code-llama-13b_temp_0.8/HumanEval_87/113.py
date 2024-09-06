
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
    def get_count_index(lst, x):
        # create a new list, count is count of x in each row
        count = []
        index = []
        count_index = []
        for i in range(len(lst)):
            count.append(lst[i].count(x))
            index.append(lst[i].index(x) if x in lst[i] else -1)
        
        for i in range(len(lst)):
            count_index.append((count[i], index[i]))
        return count_index
    
    count_index = get_count_index(lst, x)
    count_index = sorted(count_index, key=lambda x: (x[0], -x[1]))
    result = []
    for (count, index) in count_index:
        if count == 0:
            continue
        for i in range(count):
            result.append((count_index.index((count, index)), index - i))
    return result
        
        
