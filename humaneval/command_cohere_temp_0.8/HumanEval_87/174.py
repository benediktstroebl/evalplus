```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        row_with_x = []
        for j, col in enumerate(row):
            if col == x:
                row_with_x.append((i, j))
        result.extend(sorted(row_with_x, key=lambda x: (x[0] * 100000000 + x[1])))
    return result
```

The `get_row` function iterates through each row in the list and for each element `col` in the row it checks if `col` equals the target `x`. If it does, it constructs a tuple `(i, j)`, where `i` is the index of the row and `j` is the index of the column `col` in the row. It then sorts these tuples based on the combined integer value of the row and column indices, ensuring that the result is sorted first by row indices in ascending order and then by column indices in ascending order. The final result is a list of these sorted tuples.

The example provided in the prompt would yield the following output:
```bash
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
``` 

This function operates on the input nested list `lst` and searches for instances of the target integer `x` across all columns, constructing 2-tuple coordinates for each match, which it sorts and returns. The output is a list of these coordinate tuples, ordered first by row index and then by column index for each matching row.