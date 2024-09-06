```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The nested list of lists `lst` is iterated over in a nested loop. When the value `x` is found in the inner loop, the index `i` of the outer loop, and the column index `j` of the inner loop are appended to the `result` list. The list of coordinates is then sorted by the row index in ascending order and the column index in descending order, using a lambda function passed into the `sort` method. The resulting list of tuples is the desired output.