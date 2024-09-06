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

The nested list, `matrix`, is iterated through row by row. Within each row, the values are iterated through column by column. When the value `x` is encountered, a tuple of coordinates (`i`, `j`) is appended to the `result` list. The sorting function, `lambda x: (x[0], -x[1])`, sorts the results based on the row index in ascending order and the column index in descending order. The final list of sorted coordinates is returned. 

The code handles the edge cases of an empty list and a list of empty lists, returning an empty list for both cases. It also correctly handles the example inputs provided in the problem statement.