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

The function works by first creating an empty list called `result` to store our coordinates. We then iterate over each row in the nested list `lst`, using the variable `row_index` to keep track of the index of the row. Within each row, we look for the column value `x` by iterating over the columns using the variable `col_index`, and when we find it, we append a tuple representing the row and column index to our `result` list. These indices are appended as (row_index + 1, col_index + 1) to simulate row and column numbers starting from 1. The break statement makes sure that once we find the column `x` in a row, we move on to the next row without checking the remaining columns. After iterating through all rows, we sort the `result` list initially by the row index in ascending order, and within the same row, by the column index in descending order using the `sorted` function and an appropriate `key` function. Finally, we return the `result` list. 

This solution is efficient because it has a time complexity of O(n^2) in the worst case, but tends towards O(n) when the list is sorted by column. This is because it iterates over the data only once, making a pass for each row and column.