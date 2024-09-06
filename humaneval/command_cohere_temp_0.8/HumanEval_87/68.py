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

The nested list, `matrix`, is iterated through row by row. Within each row, the list is iterated through column by column. If a value matches `x`, a tuple representing the row and column index is appended to the `result` list. This list of coordinates is then sorted first by row in ascending order and then by column in descending order. The final list of coordinates is returned. 

This solution is concise and efficient, capable of handling varied row lengths and large matrices. It passes the test cases provided, checking the output against expected results.