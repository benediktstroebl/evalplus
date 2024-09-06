```python
def get_row(lst, x):
    result = []
    for row in lst:
        for j, col in enumerate(row):
            if col == x:
                result.append((row_idx + 1, col_idx + 1))
                break
        row_idx += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))
```

The nested list `lst` is iterated by the outer loop, and the inner loop cycles through each column within the current row. When the desired integer `x` is encountered in a column, a tuple `(row_idx + 1, col_idx + 1)` is constructed, where `row_idx` is the row index and `col_idx` is the column index, both starting from 0. This tuple is appended to the `result` list, and the inner loop breaks to move to the next column. After all rows have been processed, the tuples in `result` are sorted firstly by the row index in ascending order and secondly by the column index in descending order, ensuring the output meets the requirements.