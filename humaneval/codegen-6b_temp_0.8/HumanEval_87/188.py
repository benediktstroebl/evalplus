
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
    i = 0
    j = len(lst[0]) - 1

    def binary_search(lst, x):
        """
        Binary search on the list, find x and returns its position.
        If x is not in the list, return -1.
        """
        i = 0
        j = len(lst)-1
        while j > i:
            m = (i + j) // 2
            if x == lst[m][j]:
                return m
            elif x < lst[m][j]:
                j = m - 1
            elif x > lst[m][j]:
                i = m + 1
        return -1


    def get_row_coordinates(lst, x, i, j):
        """
        Get row coordinates for x.
        Y is defined as len(lst[i]) - j,
        so that in the list,
        lst[i][j], lst[i][len(lst[i]) - 1 - j] ...
        can be accessed.
        """
        ind = binary_search(lst[i], x)
        if ind == -1:
            return []

        index = i
        while index != ind:
            index = index + 1
            if index > len(lst) - 1:
                return []
        y1, y2 = i, len(lst[i]) - 1
        while index <= len(lst) - 1:
            if lst[index][j] == x:
                y1 = index
                y2 = j
                break
            index = index + 1
        return [(y1, y2)]


    def get_row_coordinates_sort_by_columns(lst, x, i, j):
        """
        Get row coordinates for x.
        Y is defined as len(lst[i]) - j,
        so that in the list,
        lst[i][j], lst[i][len(lst[i]) - 1 - j] ...
        can be accessed.
        """
        ind = binary_search(lst[i], x)
        if ind == -1:
