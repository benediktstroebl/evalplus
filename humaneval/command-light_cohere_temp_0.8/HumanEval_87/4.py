```python
def get_row(lst, x):
    """
    Return list of tuples, each of which is a coordinate - (row, columns), starting with 0.
    
    Sort coordinates initially by rows in ascending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    result = []
    for row in lst:
        result.append([row[row for index, col in enumerate(row)])
    return result
```