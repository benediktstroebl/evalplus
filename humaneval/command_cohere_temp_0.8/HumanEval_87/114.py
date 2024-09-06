```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_index + 1, column_index + 1))
                break
        row_index += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))
```

The algorithm utilizes nested loops to traverse through each element in the matrix. Upon finding a match for the target `x`, the code appends a tuple representing the current row and column indices to the `result` list. Breaking out of the inner loop ensures that only the first match is recorded for each row. Finally, the function sorts the resulting tuples first by row index in ascending order and then by column index in descending order, ensuring the output meets the specified order requirements.