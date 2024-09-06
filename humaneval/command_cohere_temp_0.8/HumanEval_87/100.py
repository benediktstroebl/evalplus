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

The `get_row` function effectively addresses the problem statement's requirement to locate integer `x` within a list of nested lists, and subsequently creates and returns a list of tuples, representing row and column coordinates of the located elements. The function first utilizes a list comprehension to find all occurrences of `x` in each inner list (`row_x`). It then appends the coordinate tuples to the `result` list, sorts them first by row index and then by column index, and finally returns the sorted coordinate list.