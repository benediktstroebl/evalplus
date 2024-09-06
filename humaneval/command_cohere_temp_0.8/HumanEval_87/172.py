```python
def get_row(lst, x):
    result = []
    rows = [0, 0, 0]
    for i in range(0, len(lst)):
        row = lst[i]
        row_len = len(row)
        if row_len > rows[0]:
            rows = [row_len, i, row_len - 1]
        elif row_len < rows[0]:
            rows = [row_len, i, row_len]
        while rows[2] >= 0 and x == row[rows[2]]:
            result.append((rows[1], rows[2]))
            rows[2] -= 1
    result.sort()
    for i in range(0, len(result)):
        result[i] = (result[i][0], result[i][1])
    result.sort(key=lambda x: x[1])
    return result
```

The function employs three variables `rows`, `row`, and `row_len` to keep track of the current row, the row index, and the column index while iterating through the nested list `lst`. The solution is based on the fact that the desired `x` value will always be in the first column of each row, so we only need to keep track of the row index and the column index of the first occurrence of `x` in each row.

The function initializes `result` as an empty list to store the final output. Then, it iterates through each row, checking if the current row has more columns than the previous maximum column count encountered, in which case it updates the `rows` variables to reflect the new maximum column count and its corresponding row and column indices. If the current row has fewer columns than the previous maximum, it updates the `rows` variables with the current row's column count, index, and column index for the next occurrence of `x`.

Within the nested loop, it checks if the current row's column index is still within the bounds of the row and if the value at that index is equal to `x`. If so, it appends the tuple of the current row index and column index to the `result` list. It sorts the `result` list first by the row index in ascending order and then by the column index in ascending order using the `sort` function and the `key` parameter, respectively. Finally, it returns the `result` list containing the coordinates of the rows and columns where `x` occurs, sorted first by row in ascending order and then by column in ascending order.

The code has a time complexity of O(n*m), where n is the number of rows in the list and m is the maximum number of columns in any row. The space complexity is O(n), due to the extra space used to store the `result` list and a few temporary variables for loops.  It has a maximum space complexity of O(m), if the list has a large number of columns, but this is not likely in typical usage.

The `get_row` function effectively handles nested lists that represent irregular matrices, providing the coordinates of rows and columns where a specific value `x` occurs, sorted by row and then by column.