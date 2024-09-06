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

The nested list, `matrix`, is iterated through row by row. Within each row, the list is iterated through column by column. When the value `x` is encountered, a tuple of coordinates is created and added to the `result` list. The tuple's elements are the row index and column index, respectively. The `result` list is then sorted first by row in ascending order and then by column in descending order, ensuring the tuples are presented in the required format. 

The problem is solved in a single code block that can be executed directly. It does not rely on any external variables and can be copied and run independently.