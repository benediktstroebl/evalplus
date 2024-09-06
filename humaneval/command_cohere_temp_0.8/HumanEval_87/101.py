```python
def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if x == cols:
            result.append((len(lst) - row.index(True), cols))
    result.sort()
    return result
```

The nested list `lst` is traversed element by element, and for each row, the column count (`cols`) is computed using `len(row)`. When `x` matches `cols`, a tuple is appended to `result` with the row index and column count. This index correlates to the row number in the matrix because we're sorting rows by their occurrence in `lst`.

To ensure the output is correctly sorted, we sort the `result` list using the `sort()` method, which arranges the tuples in ascending order first by row and then by column. Finally, the function returns the sorted `result` list.

This algorithm has a time complexity of O(n^2) due to the nested list traversal and iteration required to find the desired row. It's an optimal solution for this problem, however, given that the nested list structure is inherently unpredictable and heterogeneous.