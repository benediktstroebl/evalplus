```python
def get_row(lst, x):
    result = []
    for row in lst:
        if x in row:
            col = row.index(x)
            result.append((len(lst) - row.index(row) - 1, col))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The `get_row` function iterates through each row in the list and checks if the `x` value is present in the current row. If found, it calculates the column position of the value and appends a tuple of coordinates as (row_number, column_position) to the `result` list. The `sort` function is then used to sort the list of coordinates first by row in ascending order and then by column in descending order. Finally, the function returns the sorted `result` list.