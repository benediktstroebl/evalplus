```python
def get_row(lst, x):
    res = []
    for row in lst:
        if x in row:
            col = row.index(x)
            res.append((len(lst) - row.index(row) - 1, col))
    res.sort(key=lambda x: (x[0], -x[1]))
    return res
```

The `get_row` function iterates through each row in the list and checks if the `x` value is present in the row. If found, it calculates the column position of the value and appends a tuple of the form `(row_num, col_num)` to the `res` list. The tuple is constructed using the length of the list minus the row index minus 1 (to start row indexing from 0) and the column index of the value `x` in the current row.

The resulting list of tuples is sorted first by the row index in ascending order and then by the column index in descending order. This ensures that the tuples are presented with the row and column coordinates. 

The function returns the sorted list of tuples.