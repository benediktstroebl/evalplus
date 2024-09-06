```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, value in enumerate(row):
            if value == x:
                result.append((row_index + 1, column_index + 1))
                break
        row_index += 1
    result.sort(key=lambda x: x[1])
    return result
```

The nested list, `matrix`, is iterated through row by row. Within each row, the list is iterated through columns using `enumerate()` to keep track of the column index `j`. When the value at the current column is equal to `x`, a tuple `(row_index + 1, column_index + 1)` is created to represent the row and column indices starting from 0 and incrementally increased, and appended to `result`. The sorting is applied to the resulting list of tuples first by row index in ascending order and then by column index in ascending order using the `sort()` method with the `key` parameter set to a lambda function. Transforming the indices to 1-based indices is done within the lambda function. The final result is returned.