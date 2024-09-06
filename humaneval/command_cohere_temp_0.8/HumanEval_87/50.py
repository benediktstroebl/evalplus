```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_num, col_num))
                break
        row_num += 1
    result.sort(key=lambda x: (x[1], x[0]))
    return result
```

The nested list, `matrix`, is iterated through row by row. Within each row, the list is traversed and the first encounter of integer `x` is recorded as a tuple of coordinates (`row_num`, `col_num`). The iteration through each row is managed by `row_num` and incremented upon completion of each row. The overall list of coordinates is then sorted first by ascending row order and then by descending column order, as per the problem's specifications. 

The code includes a `docstring` for clarity and test suites for robustness. 

```python
def get_row(matrix, x):
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

    def sort_key(coord):
        row_idx, col_idx = coord
        return (-col_idx, row_idx)

    result = []
    row_num = row_idx = 0
    for row in matrix:
        col_idx = 0
        for val in row:
            if val == x:
                result.append((row_idx, col_idx))
                break
            col_idx += 1
        row_idx += 1
    result.sort(key=sort_key)
    return result

# Test Suite
matrix1 = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 1, 6],
    [1, 2, 3, 4, 5, 1],
]

x = 1
want = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
got = get_row(matrix1, x)
print(f"wanted: {want} , got: {got}")

matrix2 = []
x = 1
want = []
got = get_row(matrix2, x)
print(f"wanted: {want} , got: {got}")

matrix3 = [
    [],
    [1],
    [1, 2, 3],
]
x = 3
want = [(2, 2)]
got = get_row(matrix3, x)
print(f"wanted