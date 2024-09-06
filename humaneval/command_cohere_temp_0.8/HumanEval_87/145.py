```python
def get_row(lst, x):
    result = []
    for row in lst:
        row_counter = 0
        for val in row:
            if val == x:
                result.append((row_counter, row_counter))
                row_counter += 1
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result
```

The nested list `lst` is traversed element by element and row by row. When the value `x` is encountered, the row index is appended to the resulting list of tuples. In order to keep track of the columns' index, `row_counter` is increased whenever a value `x` is found. The resulting list of tuples is sorted by row index in ascending order and then by column index in descending order to achieve the desired sorting. Finally, the list of tuples is returned.