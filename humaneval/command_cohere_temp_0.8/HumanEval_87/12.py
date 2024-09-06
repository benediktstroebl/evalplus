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

The `get_row` function iterates through each row in the list, checking if the length of the current row matches the target value `x`. If it does, the function calculates the row's index and appends a tuple representing the row's coordinate to the `result` list. The tuples are sorted first by row in ascending order and then by column in descending order using the `sort()` method. 

This approach ensures that the tuples are correctly sorted by both row and column values, matching the specified behavior of the desired output. It is also worth noting that this solution has a time complexity of O(n log n) due to the sorting step, which is efficient enough for most practical applications.