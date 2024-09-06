```python
def get_row(lst, x):
    result = []
    for row in lst:
        if x in row: 
            result.append((row.index(x), row.index(max(row)))) 
    result.sort(key = lambda x: x[0])
    return result
```

The task is to find all occurrences of a given integer `x` in the nested list, and return list of tuples representing its coordinates, i.e. row index and column index, sorted by rows in ascending order and by columns in descending order. The function performs nested loops to go through all the rows in the list, and if a given integer `x` is found, a tuple is created with the row index and the column index, sorted by the row and then by the column. The sorting key `lambda x: x[0]` sorts the result by the row index `x[0]` in ascending order.