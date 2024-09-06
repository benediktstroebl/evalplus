```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            result.append((i, row.index(x)))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1])
    return result
```

The `get_row` function iterates through each row in the `lst` nested list. For each row, it checks if the `x` value is present in the row using the `in` operator. If found, it computes the row index `i` and the column index of `x` in the format `(row_index, column_index)`.

The resulting list of coordinate tuples is then sorted first by the row index in ascending order and then by the column index in ascending order. This ensures that the output list of coordinates is sorted initially by row and then by column within each row. Finally, it returns the sorted list of coordinate tuples.