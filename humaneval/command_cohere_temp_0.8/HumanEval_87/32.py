```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        cols = len(row)
        if cols == x:
            result.append((i, cols))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1])
    return result
```

The `get_row` function iterates through each row in the `lst`, checks if the length of the row matches the target `x`, and appends the corresponding `(row_num, col_num)` tuple to the `result` list. The tuples are then sorted first by row number and then by column number, assuming the matrix is row-major order. The resulting list of tuples is returned.

This approach ensures that the result is a list of tuples representing the coordinates of rows with exactly `x` columns, sorted first by row and then by column.