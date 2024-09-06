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

The code iterates through each element in the matrix and checks if the value matches the target `x`. If it does, the current row and column index are appended in a tuple and added to the `result` list. The list of tuples is then sorted first by the row index in ascending order and then by the column index in descending order using the `sort` method and a lambda function as the sorting key. Finally, the function returns the `result` list of sorted tuples. 

This solution is efficient due to its single-pass iteration and minimal computational overhead for sorting.