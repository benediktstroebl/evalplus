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

The `get_row` function iterates through each row in the list and checks if the `x` value is present in each row. If found, it calculates the column position of the value and appends a tuple of the form `(row_num, col_pos)` to the `res` list. The tuple is constructed using the length of the list minus the row index minus 1 (to ensure the row numbers start from 0) and the column position. The sort is conducted using the `lambda` function, first by row in ascending order and then by column in descending direction to ensure the desired output order.