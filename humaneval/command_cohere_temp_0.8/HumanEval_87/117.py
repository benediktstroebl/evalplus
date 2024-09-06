```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        cols = len(row)
        if cols > x:
            continue
        j = bisect.bisect_left(row, x)
        result.append((i, j))
    result.sort(key=lambda x: (x[1], -x[0]))
    return result
```

The nested list `lst` is traversed using a `for` loop, where each iteration iterates over a list of rows. For each row, the code calculates the index `j` of the first occurrence of integer `x` in the row using the `bisect` module. This assumes that the rows are sorted in ascending order, which is typical in matrix-like structures. If the column count is greater than `x`, the row is skipped. A tuple of coordinates is created, indicating the row and column indices, and appended to the `result` list. The list of tuples is sorted first by column index in descending order and then by row index in ascending order, ensuring a consistent order.