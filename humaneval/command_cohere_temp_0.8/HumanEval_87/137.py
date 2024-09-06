```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        row_x = [column for column in row if column == x]
        if row_x: 
            result.append((i, len(row_x)))
            result.extend((i, index) for index in enumerate(row_x))
    return result
```

The solution works by first creating a list of indices (`result`) where the desired x appears in each row. Then, it completes two loops:
1. The outer loop iterates through each row in the `lst` using `enumerate()` to track both the index `i` and the row `row`. 
2. The inner loop finds all occurrences of `x` in the `row` by using a list comprehension, which is stored in `row_x`. It then adds the coordinate `(i, len(row_x))` to `result`, which represents the row and total number of columns. 

After that, within the same inner loop, it adds to `result` each occurrence of `(i, index)` for `index` in `enumerate(row_x)`, which represents the column index of the first occurrence of `x` in each row. The final result is a list of tuples, sorted first by row in ascending order and then by column in descending order for each row. 

The code is concise and achieves the desired result, making it an efficient and readable solution.