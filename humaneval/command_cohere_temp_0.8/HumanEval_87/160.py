```python
def get_row(lst, x):
    result = []
    rows = [0, 0, 0]
    for i in range(0, len(lst)):
        row = lst[i]
        cols = len(row)
        if cols == x:
            result.append((rows[0], cols))
            rows[0] += 1
        elif cols > x:
            result.append((rows[1], cols))
            rows[1] += 1
        else:
            result.append((rows[2], cols))
            rows[2] += 1
    return sorted(result, key=lambda x: (x[0], x[1]))
```

The function works as follows:
1. Initialize an empty list `result` to store the found coordinates.
2. Initialize three variables `rows`, which represent the counts of rows with less, equal, and more columns than `x`.
3. Loop through the list of rows lst.
4. For each row, determine the number of columns cols.
5. If cols is equal to `x`, append a tuple representing the current row's index and the column count to `result` and increment the count of rows with equal columns.
6. If cols is greater than `x`, append a tuple representing the current row's index and the column count to `result` and increment the count of rows with more columns.
7. If cols is less than `x`, append a tuple representing the current row's index and the column count to `result` and increment the count of rows with fewer columns.
8. After looping through all the rows, sort the `result` list by the tuple key `(row_index, column_count)` in ascending order for rows and column count in descending order for rows.
9. Return the sorted `result` list.

This approach efficiently computes the desired coordinates without unnecessary iterations or redundant calculations.