```python
def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            temp = []
            for i, col in enumerate(row):
                if col == x:
                    temp.append((i+1, len(row_x[0])))
            result.extend(sorted(temp, key=lambda x: x[1]))
    return result
```

The modular approach to finding the desired row and column indices is to use a list comprehension for each row. This allows us to then process the resulting list of column indices, sorting them by column values using the `sorted` function. From there, we can extract the row and column for each x value, constructing the return list of tuples. Importantly, we use `enumerate` to track both row index and column index, avoiding manual tracking with `x` and `y` variables, which would be error prone. The output is a list of tuples, sorted first by row, then inside each row by column value. 

This approach ensures a straightforward, easily understandable implementation, tolerant to diverse data shapes.