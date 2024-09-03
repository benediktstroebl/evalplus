```python
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
    rows = [lst[x:x+i] for x in range(len(lst)) for i in range(1, x//2+1)]
    return sorted((row, col) for row in rows for col in range(row[0]))
```

The code implements a function `get_row` that takes a list `lst` and an index `x` as input. The function then splits the the list into a list of sublists based on index `x`, and then sorts the sublists by rows in ascending order. Finally, the function returns a list of tuples containing the row and column indices of each element in the original list.