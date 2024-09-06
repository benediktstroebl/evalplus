```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The nested list of lists `lst` is traversed element by element and within each list, each element is checked against the desired `x`. The resulting coordinates are tuples of (row index, column index) and are appended to the `result` list. The list of tuples is then sorted by row index in ascending order and by column index in descending order, as required by the problem statement.