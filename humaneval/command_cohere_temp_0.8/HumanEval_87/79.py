```python
def get_row(lst, x):
    result = []
    for row in lst:
        for col in row:
            if col == x:
                result.append((row, col))
    result.sort(key=lambda x: (x[0] + 1, x[1]))
    return result
```

The `get_row` function iterates through each list in the nested list `lst`, and for each list it iterates over each element checking if it matches the desired integer `x`. If a match is found, a tuple of coordinates (`row`, `col`) is appended to the `result` list. The list of tuples is then sorted first by row in ascending order and then by column in ascending order using the `sort` method with an appropriate `key` parameter. Finally, the function returns the sorted list of tuples. 

This approach ensures that the tuples are sorted first by row and then by column, as required by the problem statement.