```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_index + 1, column_index + 1))
                column_index += 1
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result
```

The algorithm utilizes two for loops to traverse the matrix row by row and column by column. While iterating, it tracks the row index `row_index` and column index `column_index` to maintain the coordinates. When a value `x` is encountered, a tuple is created with the current coordinates, appended to the `result` list, and the column index is incremented to move to the next column. The final step sorts the list of tuples first by the row in ascending order and then by the column in descending order.