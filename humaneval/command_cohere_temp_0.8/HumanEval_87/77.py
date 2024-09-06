```python
def get_row(lst, x):
    result = []
    for row in lst:
        for j, col in enumerate(row):
            if col == x:
                result.append((row_index + 1, col_index + 1))
                break
        row_index += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))
```

The `get_row` function implements the given problem through the following steps:
1. The function iterates through each row in the nested list `lst`.
2. For each row, it iterates through the columns using the `enumerate` function, and when it finds the value `x`, it appends a tuple `(row_index, col_index)` to the `result` list.
3. The tuples are sorted in ascending order based on the row index and then in descending order based on the column index, using a lambda function in the `sorted` function.

This solution effectively finds the coordinates of the value `x` in the list and returns them sorted by row and column indices as required by the problem statement.