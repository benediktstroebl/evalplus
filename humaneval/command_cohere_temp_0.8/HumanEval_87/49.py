```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The `get_row` function iterates through each nested list within the input `lst`, and for each list iterates through its elements. When a match is found for the integer `x`, a tuple (`i`, `j`) is appended to the `result` list, representing the row and column indices of the match. The list of tuples is then sorted first by the row index in ascending order and then by the column index in descending order. 

This sorting ensures that the resulting list of tuples is organized in a consistent format, ready for further processing or display.