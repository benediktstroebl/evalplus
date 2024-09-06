```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        row_x = [col for col in row if col == x]
        if row_x: 
            result.append((i, len(row_x)))
            result.extend([(i, j) for j in range(len(row_x) - 1, -1, -1)])
    return result
```

The `get_row` function accepts two parameters: a list of lists `lst` and an integer `x`. It searches through the list `lst` for elements equal to `x` and constructs tuples containing the row index and the number of columns in the row. The resulting list of tuples is sorted first by row index in ascending order and then by column count in descending order.

The algorithm works as follows:
1. Initialize an empty list called `result` to store the resulting tuples.
2. Iterate through each row in the nested list `lst` using the `enumerate` function which provides both the index `i` and the row `row` simultaneously.
3. For each row, create a list called `row_x` that contains all the elements in the row that match the desired value `x`.
4. If `row_x` contains elements, append the tuple `(i, len(row_x))` to `result`, representing the row index and column count.
5. Additionally, create and append to `result` any necessary intermediate tuples `(i, j)` for all column indices `j` within the current row, from right to left (`len(row_x) - 1, -1, -1`) since the output should be sorted by column in descending order.
6. Repeat the process for all rows in `lst` until `x` is found in every row.
7. Return the fully populated and sorted `result` list.

The tests included with the problem demonstrate various scenarios for validation, such as an empty list, a list with empty rows, or a list with rows of different lengths. The output of the function should correspond to the expected output provided in the test cases.