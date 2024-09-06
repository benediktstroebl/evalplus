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

The `get_row` function iterates through each row in the list and checks if the `x` value is present in each row. If found, it calculates the column position of the value and appends a tuple of the form `(row_number, column_number)` to the `result` list. The tuple is constructed using the length of the list minus the row index minus 1 (to start indexing from 0) and the column index `(-x[1])` to ensure columns are sorted in descending order for sorting the final result. Finally, the function returns the sorted list of coordinates.