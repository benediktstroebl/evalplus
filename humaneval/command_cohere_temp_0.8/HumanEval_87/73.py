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

The code iterates through each element in the matrix and checks if the value matches the target `x`. If it does, the current row and column index are appended in a tuple, and sorted by row in ascending order and column in descending order. This way, the coordinates are sorted initially by rows in ascending order and then by columns in descending order within each row.