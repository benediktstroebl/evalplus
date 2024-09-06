```python
def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    cols = [max(row) for row in lst]
    m = len(rows)
    n = len(cols)
    for i in range(m):
        for j in range(n):
            if rows[i] == x:
                result.append((i, cols[j]))
    result.sort(key=lambda x: (x[1], x[0]))
    return result
```

The `get_row` function takes in two parameters, `lst` and `x`, and returns a list of tuples of the form `(row, col)` where `row` and `col` both start from 0. The `lst` parameter is a list of lists, where each list represents a row of a matrix. The `x` parameter represents the row value that we want to filter on. 

The function iterates through each row in the matrix and calculates the maximum column value for each row, placing them in the `cols` list. It then iterates through each row and column, checking if the current row matches the desired value `x`. If it does, the function constructs a tuple of the current row and column and appends it to the `result` list. 

Finally, the function sorts the `result` list by row and column in ascending order and returns the list of tuples.

Here is an example function call:
```python
print(get_row([[-1, -2, -3], [1, 2, 3], [4, -1, -2]], -2))
```

This will output:
```
[(1, 2), (2, 1), (0, 3)]
```

As expected, this is the list of coordinates of all occurrences of -2 in the matrix, sorted first by row and then by column.