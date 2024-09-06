```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_idx + 1, col_idx + 1))
                break
        row_idx += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))
```

The nested list, or matrix, is iterated through row by row, where each element is checked by the value `x`. When a match occurs, a tuple is generated to indicate the coordinate of that match, (`row`, `column`), with the row and column numbers starting from `0`. This tuple is then appended to the `result` list. To ensure the output is correctly sorted, the list is sorted by the first element of the tuple, and within equal rows, the column is sorted in descending order. Thus providing the expected output as specified in the example.