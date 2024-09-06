```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_idx + 1, col_idx + 1))
                break
        row_idx += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))
```

The nested list, or matrix, is iterated through row by row, where each element is checked by the value `x`. When a match occurs, a tuple is created with the current index (representing the row) and the current column index, `enumerate()` helps to keep track of the column index, the index is incremented by 1 to represent row and column indices starting from `1`. Sorting is applied to the list of tuples using a custom sorting key that sorts by the row and then by the column in descending order. This way, the coordinates are sorted first by rows and then by columns in column-major order.