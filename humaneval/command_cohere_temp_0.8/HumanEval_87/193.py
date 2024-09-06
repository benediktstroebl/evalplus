```python
def get_row(lst, x):
    out = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                out.append((i, j))
    out.sort(key=lambda x: (x[0], -x[1]))
    return out
```

The nested list of lists `lst` is traversed element by element, and the inner list is traversed element by iteration through each inner list, the `enumerate` function is used for easier access to the index `i` and the value `row` from the iterable `lst`, whenever the value at index `j` of the current `row` is equal to `x`, a tuple of coordinates `(i, j)` is constructed and appended to the output list `out`. After traversing the entire list, the coordinates are sorted first by the row index in ascending order and then by the column index in descending order using the `sort` method with a lambda function `key=lambda x: (x[0], -x[1])` as the sorting key, the resulting list of coordinates is returned. 

The code should correctly solve the problem for the given examples and pass the tests.