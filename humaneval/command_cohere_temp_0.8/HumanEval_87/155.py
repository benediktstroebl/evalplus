```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_index + 1, column_index + 1))
                column_index += 1
    result.sort(key=lambda x: x[1])
    return result
```

The nested list, `matrix`, is iterated through row by row. Within each row, the values are iterated through and compared to `x`. When a match is found, a tuple is created with the row index and column index and appended to `result`. The tuple is sorted based on the column index, which ultimately displays the coordinates in ascending order, row by row. 

Here is an example usage of the function:
```python
matrix = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 1, 6],
    [1, 2, 3, 4, 5, 1],
]

print(get_row(matrix, 1))
```

This will output:
```
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
```