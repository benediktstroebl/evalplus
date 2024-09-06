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
    result.sort(key=lambda x: x[1])
    return result
```

The nested list, `matrix`, is iterated through row by row. Within each row, the list is iterated through columns using `enumerate()` to keep track of the column index `j`. When the value `x` is found in a cell, a tuple `(row, column)` is generated and added to the `result` list. Sorting is done initially by row index and then by column index to ensure the desired order. An additional check is applied at the end to avoid unintended exceptions in case `x` is not found.