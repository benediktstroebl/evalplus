```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        row_match = [col for col in row if col == x]
        if row_match:
            result.append((i, len(row_match)))
            result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The algorithm works by using a list comprehension to filter out the list lst by checking if the value `x` is present in each row, if so, a tuple is created with the index `i` and the number of columns `x`, this value is appended to the `result` list. The list is sorted by the index in ascending order and the columns in descending order to comply with the requested format. The solution is returned.