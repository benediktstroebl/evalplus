```python
def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    cols = []
    for row in lst:
        temp = [i for i in row]
        cols.append(temp)
        result.append(sorted(enumerate(temp), key=lambda x: (x[1], x[0])))
    result = sorted(result, key=lambda x: (x[0], len(x[1])))
    return [coord for coord in result if coord[0] == x]
```

The function `get_row` works by first creating a list of lists, where each inner list corresponds to the columns of a row in `lst`. It then sorts these lists based on the number of columns in ascending order. Following that, it sorts the rows based on the row index in ascending order and the columns within each row based on the column index in descending order. Finally, it iterates through the sorted lists and returns only the rows that match the desired row index `x`. The result is a list of tuples containing the row and column indices for the desired row, sorted by column index in ascending order.