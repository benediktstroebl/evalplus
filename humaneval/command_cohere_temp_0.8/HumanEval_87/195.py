```python
def get_row(matrix, x):
    result = []
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The nested list, `matrix`, is iterated through row by row. Within each row, the values are iterated through column by column. When the value `x` is found in the list, a tuple of coordinates is created as `(i, j)`, where `i` is the row number and `j` is the column number. This tuple is then appended to the `result` list. Once all rows have been searched, the tuples are sorted first by row in ascending order and then by column in descending order using the `sort` method with the `key` argument set to identify the sorting mechanism. 

This code matches the given `Examples` and should pass any tests related to those examples.