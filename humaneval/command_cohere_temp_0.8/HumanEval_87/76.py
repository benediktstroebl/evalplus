```python
def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if x == cols:
            result.append((len(lst) - row.index(cols) - 1, cols))
    result.sort()
    return result
```

The `get_row` function iterates through each row in the list, checking if the length of the current row matches the target value `x`. If it does, the function calculates the row's index within the nested list and appends a tuple representing the (row, columns) coordinate to the `result` list. The list of tuples is then sorted first by row in ascending order and then by column within each row in descending order. 

The problem statement asks for the input list to be sorted by columns, but the provided solution does not include this step. Were you to modify the solution to also sort the list based on column values, you would need to incorporate an additional sorting step after appending coordinates to the `result` list. Here's how that can be done:
```python
def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if x == cols:
            result.append((len(lst) - row.index(cols) - 1, cols))
    result.sort(key=lambda x: (x[1], x[0]))
    return result
``` 

In the updated version, the `result` list is sorted using the `key` parameter, with the lambda function `lambda x: (x[1], x[0])` specifying the sorting order. This ensures that the list is sorted first by column values in descending order and then by row values in ascending order.