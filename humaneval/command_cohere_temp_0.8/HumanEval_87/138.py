```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        cols = len(row)
        if cols == x:
            result.append((i, cols))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1])
    return result
```

The `get_row` function iterates through each row in the list and checks if the column length matches the target value `x`. If it does, a tuple containing the row index and column length is appended to the `result` list. The tuples are then sorted first by row index in ascending order and then by column length in ascending order to ensure the desired order of coordinates. Finally, the function returns the sorted tuple list. 

This approach guarantees the correct retrieval of coordinates corresponding to rows with exactly `x` columns, while also sorting them first by row and then by column for clarity.