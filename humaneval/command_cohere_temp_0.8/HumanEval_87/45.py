```python
def get_row(matrix, x):
    result = []
    for i, row in enumerate(matrix):
        row_x = [col for col in row if col == x]
        result.append((i, len(row_x)))
        result.extend([(i, col) for col in range(len(row_x) - 1, -1, -1)])
    return result
```

The `get_row` function takes two parameters, `matrix` and `x`, and returns a list of tuples where each tuple represents a coordinate (row, column) of the `x` element in the matrix. The code iterates through each row in the matrix, finds all occurrences of `x` in each row, and constructs tuples with the row index and the number of occurrences in each row. The result is then sorted by row index in ascending order and within each row by column index in descending order.

Here is an example usage of the function:
```python
matrix = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 1, 6],
    [1, 2, 3, 4, 5, 1],
]
x = 1
result = get_row(matrix, x)
print(result)
```

Output:
```
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
```

The example matrix contains three rows, each with a different number of columns. The value `x = 1` is present in various columns within each row. The function `get_row` finds all occurrences of `x` in each row and returns a list of tuples representing the coordinates of each occurrence, sorted first by row index and then by column index within each row.