```python
def get_row(lst, x):
    result = []
    rows = []
    for row in lst:
        if x in row:
            cols = len(row)
            result.append((len(rows), cols))
            rows.append(row)
    if x not in rows:
        return []
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The `get_row` function iterates through each row in the list and checks if the `x` value is present in the row. If found, it calculates the column count and appends a tuple of (row_num, column_count) to the `result` list. This is done for each row that contains `x`, and the result is sorted first by row number and then by column count in descending order, meeting the criteria specified in the problem statement. The function returns the sorted list of coordinate tuples.