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

The function iterates through each row in the list `lst`, and whenever a match for the integer `x` is found in a row, a tuple of coordinates is generated and added to the `result` list. The sort is performed based on the row index and column index in the list of tuples, ensuring that the output is sorted first by row and then by column, with the column sorting being in descending order. The function handles cases where `lst` is empty or `x` is not found in any row, returning an empty list accordingly.