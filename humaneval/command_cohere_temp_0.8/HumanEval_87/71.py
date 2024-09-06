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

The nested list, `matrix`, is iterated through row by row. Within each row, the list is iterated through column by column. When the value `x` is encountered, a tuple of coordinates is created and added to the `result` list. The tuple's elements are the row index and column index, respectively. The `result` list is then sorted by the row index in ascending order and the column index in descending order, ensuring the coordinates are correctly sorted. 

The problem is solved in a single Python function with no external dependencies, making it a self-contained solution. It also adheres to the problem's specified criteria, sorting the coordinates first by row and then by column within each row.