```python
def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if x == cols:
            result.append((len(lst) - row.index(True), cols))
    result.sort() by= (lambda x: x[1], lambda x: x[0])
    return result
```

The function iterates through each row in the list and checks if the value of `x` corresponds to the number of columns in the current row. If it does, a tuple is created containing the row index and column value and added to the `result` list. The list of tuples is then sorted first by row index in ascending order and then by column value in ascending order using the `sorted` function with a custom sorting key. 

The code assumes that the input list contains at least one row and the value of `x` is contained in at least one of the rows. If the input list is empty or `x` is not found in any of the rows, an empty list is returned.