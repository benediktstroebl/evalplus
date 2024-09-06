```python
def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if x == cols:
            result.append((len(lst) - row.index(True), cols))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The nested list `lst` is traversed element by element, and for each row, the column count is computed and stored in the `cols` variable. If the column count matches the target `x`, a tuple is created and appended to the `result` list. The tuple contains the row index and column count, but note the unusual sorting key: `(x[0], -x[1])`. This sorts the results first by row index in ascending order, and then by column count in descending order. Finally, the function returns the `result` list of tuples.