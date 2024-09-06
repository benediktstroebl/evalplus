```python
def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            result.append((idx, len(row_x)))
            result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The solution works by using a list comprehension to filter out the rows that contain the integer `x`, and then creating a list of tuples that contain the index `idx` and the number of columns in the row `x`, sorted by the index in ascending order and the number of columns in descending order. The resulting list is then returned.