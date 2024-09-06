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

The nested list, `matrix`, is iterated through row by row. Within each row, the value `x` is searched for in the column, and the coordinate `(i, j)` is appended to the `result` list if found. The list of coordinates is then sorted first by row in ascending order and then by column in descending order using the `sort` method and a lambda `key` argument. The resulting list of tuples is returned. 

This solution should be compatible with the example use cases provided. Let me know if you would like me to explain any part of the code in more detail.