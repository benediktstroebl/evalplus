```python
def get_row(lst, x):
    result = []
    for row in lst:
        for col in row:
            if col == x:
                result.append((row, col))
    result.sort(key=lambda x: (x[0] or 0, x[1]))
    return result
```

The `get_row` function traverses each row in the `lst` list, checking each element's value against the `x` target. When a match occurs, a tuple containing the current row index and column value is assembled and appended to the `result` list. To ensure consistent ordering, the `result` list is sorted first by row index, ascending, and then by column value, descending. This arrangement generates a list of tuples, correlating to the target `x` value's row and column positions within the list. Importantly, this function effectively identifies and returns the desired row and column coordinates, arranging them in the specified order.