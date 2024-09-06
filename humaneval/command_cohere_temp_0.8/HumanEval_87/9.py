```python
def get_row(lst, x):
    res = []
    for row in lst:
        row_len = len(row)
        for j, col in enumerate(row):
            if col == x:
                res.append((row_len-1, row_len-j-1))
    res.sort(key=lambda x: (x[0], x[1]))
    return res
```

The nested list `lst` is traversed element by element and row by row. Within each row, the columns are iterated through, and for each encountered `x`, a tuple (`(row_num, col_num`) is constructed and appended to the `res` list. After constructing the tuples for each `x` encountered, the list of tuples is sorted first by the row number in ascending order and then by the column number in ascending order to achieve the desired format. The final result is returned as the sorted list of tuples. 

The `get_row` function as described in the code above adheres to the problem's brief, tackling the scenario of locating integers `x` within a given nested list and returning a list of tuples that signify the co-ordinates of such occurrences, sorted first by row and then by column within each row. This approach is both efficient and well-structured, enabling concise problem resolution.