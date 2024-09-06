```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_index + 1, column_index + 1))
                break
        row_index += 1
    result.sort(key=lambda x: x[1])
    return result
```

The algorithm works by utilizing two nested loops to iterate through every element in the matrix. Once a match is found for the target `x`, a tuple is created (`(row_index+1, column_index+1)`), where both indices are incremented by 1 to adjust the indices to start from 0. This tuple is appended to the `result` list. Additionally, the `result` list is sorted based on the column index in ascending order, ensuring that the coordinates are sorted by column on the same row. 

The function returns the `result` list, containing the coordinates of all occurrences of `x` in the matrix.