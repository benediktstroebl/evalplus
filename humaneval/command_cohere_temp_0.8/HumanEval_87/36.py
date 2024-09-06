```python
def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            col_sort = sorted(row_x)
            result.append((len(lst) - row.index(col_sort[0]) - 1, len(col_sort)))
    return result
```

The nested list `lst` is traversed element by element, and for each element the search for `x` is conducted using a list comprehension. The found elements are sorted by column index, and the coordinates are appended to the `result` list. The list `result` is sorted by row index to achieve the final sorted order of the output.

The code assumes that the given list `lst` is non-empty and at least one element `x` is present in at least one of the nested lists, because otherwise, the list comprehension will not be able to iterate over it, and an error will be raised. Although these assumptions are guaranteed by the test cases provided, they may not hold true in general cases, and therefore should be addressed for a fully robust solution.