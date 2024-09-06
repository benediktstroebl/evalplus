```python
def get_row(lst, x):
    result = []
    for row in lst:
        for j, col in enumerate(row):
            if col == x:
                result.append((row_index + 1, col_index + 1))
                break
        row_index += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))
```

The function uses nested loops to traverse the list of rows and columns within each row to find the `x` value. Once the value is found, a tuple indicating the row and column index is appended to the `result` list. To maintain the correct order, the indices are appended as (row, column) and sorted by the row in ascending order and column in descending order. The final list of coordinates is returned. 

The `result` list is sorted to ensure consistent output order, as mentioned in the exercise. While not the most efficient solution due to nested loops, the code is concise and easy to understand. 

This approach has a time complexity of `O(n * m * p)`, where `n` is the number of rows, `m` is the number of elements in each row, and `p` is the number of occurrences of `x`.