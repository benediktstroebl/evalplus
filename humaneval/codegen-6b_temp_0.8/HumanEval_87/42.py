
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
    def index_of_list(lst, x):
        i = 0
        while i < len(lst):
            if x == lst[i]:
                return i
            i += 1

        return None

    lst = sorted(lst, key=lambda x: x[0])
    lst = sorted(lst, key=lambda x: x[1], reverse=True)
    lst = sorted(lst, key=lambda x: x[0])

    result = []
    for i in range(len(lst)):
        result.append((index_of_list(lst[i], x), i))

    return result


assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
assert get_row([[1], [2, 3], [4], [5, 6]], 3) == [(2, 1), (2, 3)]
assert get_row([[1, 2], [3, 4], [5, 6]], 3) == [(1, 1), (1, 2)]
assert get_row([[1, 2], [3, 4], [5, 6], [7, 8]], 9) == [(1, 1), (1, 2), (1, 3), (1, 4)]
assert get_row([[1, 2], [3, 4], [5, 6]], 3) == [(2, 1), (2, 2), (2, 0)]
assert get_row([[1, 2], [3, 4], [5, 6]], 7) == [(1, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
assert get_row([[], [1], [1, 2, 3], [1, 2, 3]], 1) == [(0, 0), (0, 1), (0, 3), (1, 0), (1, 3)]
assert get_row([[], [1], [1, 2], [1]], 1) == [(0, 0), (0, 1)]
assert get_row([[], [1],