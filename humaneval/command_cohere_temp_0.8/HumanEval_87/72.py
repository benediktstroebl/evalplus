```python
def get_row(matrix, x):
    result = []
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The nested list, `matrix`, is iterated through row by row. Within each row, the list is iterated through column by column. When the value `x` is encountered, a tuple of coordinates is created as `((row index), (column index))`. This tuple is then appended to the `result` list. To sort the coordinates by row in ascending order, and by column in descending order, the `result` list is sorted using a lambda function at the end.