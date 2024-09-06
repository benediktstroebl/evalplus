```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_num, column_num))
                break
        row_num += 1
    result.sort(key=lambda x: (x[1], x[0]))
    return result
```

The nested list, `matrix`, is iterated through row by row. Within each row, the list is traversed and the first encounter of integer `x` is recorded and appended to `result` as a tuple of coordinates. The row number increments accordingly along with the column index (`column_num`), which is reset to zero for each new row.

To adhere to the stipulated requirement of sorting the coordinates first by row in ascending order and then by column in descending order, `result` utilises the `sort()` method with the `key` argument, utilising a lambda function to sort by the tuple `(x[1], x[0])`.