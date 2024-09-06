```python
def get_row(lst, x):
    result = []
    for row in lst:
        if x in row: 
            result.append((idx, len(row)))
            result.sort(key = lambda x: x[1])
    result.sort(key = lambda x: x[0])
    return result
```

The `get_row` function iterates through each row in the list, checking if the `x` value is present in each row. If found, it includes the index `idx` and the column width `len(row)` in the result, sorted first by row index and then by column width. Any missing values result in an empty list being returned.