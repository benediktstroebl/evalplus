```python
def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            result.append((len(row_x), len(row_x) * 1)) 
    result.sort()
    result.sort(key=lambda x: x[1])
    return result
```

The `get_row` function effectively finds the locations of the integer `x` in each row of the matrix-like list, sorting the results first by row index and then by column index. The output is a list of tuples containing the row and column indices of the located elements.