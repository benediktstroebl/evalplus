
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
    row = lst
    col = [0] * len(lst[0])
    lst = [lst]
    for i in range(1, len(lst)):
        lst = lst[1:]
    for i in range(len(row)):
        col[row[i][0]] += row[i][1]
    for i in range(len(col)):
        if col[i] > 0:
            col[i] -= row[i][1]
            col[lst[0][i]] -= row[i][1]
            for j in range(len(lst)):
                lst[j][col[lst[j][i]]] = lst[j][col[lst[j][i]]] + row[i][1]
            break
    return lst[0]

if __name__ == "__main__":
    t = [
      [1, 2, 3, 4, 5, 6],
      [1, 2, 3, 4, 1, 6],
      [1, 2, 3, 4, 5, 1]
    ]
    x = 1
    print(get_row(t, x))