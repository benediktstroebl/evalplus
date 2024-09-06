```python
def get_row(lst, x):
    result = []
    for row in lst:
        for j, col in enumerate(row):
            if col == x:
                result.append((row_index + 1, column_index + 1))
                row_index += 1
                column_index = 0
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1])
    return result
```

The nested list, `lst`, is iterated through row by row. Within each row, the list is traversed and checked for elements equal to `x`. When a match is found, a tuple is created representing the row and column index of that match. These tuples are appended to the `result` list. To ensure sorting by row and then by column, two sorting operations are applied:
1. The first sort leverages the lambda function `lambda x: x[0]` to initially sort the tuples by the row index.
2. The second sort employs another lambda function, `lambda x: x[1]`, to sort the tuples within each row by their column index.

This approach guarantees that the resulting list of tuples is ordered first by row, then by column.