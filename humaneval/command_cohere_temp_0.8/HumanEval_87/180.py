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

The nested list, or matrix, is iterated through row by row, where each element is checked by the value `x`. When a match occurs, a tuple is generated to be added to the `result` list, which is sorted by the row in ascending order, and columns in descending order, with the help of the `sorted` function and a lambda function for sorting.