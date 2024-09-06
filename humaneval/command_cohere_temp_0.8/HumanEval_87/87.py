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

The nested list of lists `lst` is iterated over with nested loops, and the values `x` are accumulated in the `result` list in the form of tuples (`i`, `j`) representing the index `i` of the row and the index `j` of the value within the row. The `sort` function is then used to sort the values of `result` using the `key` parameter to sort by the tuple `(-x[0], -x[1])`, sorting the rows in ascending order and the columns in descending order. Finally, the `result` list is returned.