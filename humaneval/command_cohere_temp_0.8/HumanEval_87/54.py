```python
def get_row(lst, x):
    result = []
    for row in lst:
        row_len = len(row)
        for j, col in enumerate(row):
            if col == x:
                result.append((row_len-1, row_len-j-1))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The nested list, `lst`, is iterated over row by row. For each element in each row, it checks if it matches the target `x`, if it does, a tuple representing the row and column index is generated and appended to the `result` list. The `result` list is then sorted first by row index in ascending order and then by column index in descending order using the `sort` method and a lambda function as the sorting key. Finally, the function returns the `result` list of tuples.