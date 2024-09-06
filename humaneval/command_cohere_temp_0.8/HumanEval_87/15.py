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

The nested list, `matrix`, is iterated through row by row. Within each row, the list is iterated through column by column. When the value `x` is found in a cell, a tuple of coordinates is created and added to the `result` list. The tuple's elements are the row number and column number, respectively. To ensure the coordinates are sorted firstly by row and then by column, the `result` list uses the `sort` method with a custom sorting key via the `lambda` function. The output is the list of sorted coordinates. 

This solution works correspondingly for the examples provided in the prompt.