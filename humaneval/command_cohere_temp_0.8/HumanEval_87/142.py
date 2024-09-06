```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            result.append((i, row.index(x)))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result
```

The `get_row` function iterates through each row in the list `lst`, and for each row, it checks if the integer `x` is present in the row. If found, it includes a tuple `(i, row.index(x))` in the `result` list, where `i` is the row number. The tuples are then sorted first by row number in ascending order and then by column position in descending order using the `sort` method with appropriate `key` functions. Finally, it returns the sorted list of tuples.