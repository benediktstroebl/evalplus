```python
def get_row(lst, x):
    result = []
    for row in lst:
        if x in row:
            result.append((row.index(x), len(row)))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The `get_row` function iterates through each row in the list and checks if the `x` value is present in each row. If found, it computes the row index and column length into a tuple and appends it to the `result` list. The resulting list of tuples is then sorted first by row index in ascending order and then by column length in descending order using the `sort` method with a custom sorting key. 

This algorithm has a time complexity of `O(n * m)`, where `n` is the number of rows in the list and `m` is the maximum number of columns in any row. This is because the algorithm iterates through each cell in the matrix once, performing a constant-time operation on each cell.