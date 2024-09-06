```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_index + 1, column_index + 1))
                break
        else:
            continue
        row_index += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))
```

The `get_row` function iterates through each row in the matrix and finds the indices of the value `x` in each row, it then constructs a tuple of coordinates (row, column) for each match and appends it to the `result` list. The output is sorted first by the row index in ascending order and then by column index in descending order to achieve the desired sorting requirement. The `else` and `continue` statements handle the case where `x` is not found in some rows.