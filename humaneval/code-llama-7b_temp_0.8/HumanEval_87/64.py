
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
    if len(lst) == 0:
        return []
    if len(lst[0]) == 0:
        return []
    
    def get_row_helper(i, lst, x, ans):
        if i == len(lst):
            return ans
        if x in lst[i]:
            ans.append((i, lst[i].index(x)))
        # add the smaller index first
        ans = get_row_helper(i+1, lst, x, ans)
        # then add larger index
        for j in range(len(lst[i])-1, -1, -1):
            if x == lst[i][j]:
                ans.append((i, j))
        ans = get_row_helper(i+1, lst, x, ans)
        return ans
    
    return sorted(get_row_helper(0, lst, x, []), key=lambda a: (a[0], -a[1]))
