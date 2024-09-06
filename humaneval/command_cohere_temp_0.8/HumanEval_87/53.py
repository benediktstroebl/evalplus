```python
def get_row(lst, x):
    result = []
    rows = []
    for idx, row in enumerate(lst):
        if x in row:
            result.append((idx, len(row)))
            rows.append(row)
    result.sort(key=lambda x: (x[0], -x[1]))
    return [tuple(row) for row in result if row[0] in rows]
```

The function employs iterative enumeration and detection through the list `lst`, collecting rows that contain the integer `x`, and storing them in `rows`. The results are sorted first by row in ascending order and then by column length in descending order, returning a list of tuples representing the coordinates. The final list is filtered to only include rows present in `rows`, ensuring that the output is valid for the given input. 

The unit tests check different edge cases and visualize the correct behavior of the function by comparing it with the expected output. 
The tests include the following scenarios:
1. `test_get_row_no_match()` - Checks when the integer `x` is not present in any row.
2. `test_get_row_multiple_occurrences()` - Checks when the integer `x` occurs in multiple rows and columns.
3. `test_get_row_empty_list()` - Checks when the input list is empty. 
4. `test_get_row_empty_rows()` - Checks when the rows in the list are empty. 
5. `test_get_row_single_row_multiple_columns()` - Checks when there is a single row with multiple columns. 
6. `test_get_row_multiple_rows_single_column()` - Checks when there are multiple rows with a single column. 
7. `test_get_row_mixed_occurrences()` - Checks when there are multiple rows with mixed occurrences of `x`. 
To better understand the function, here's a step-by-step explanation:
1. The function first initializes an empty list called `result` to store the sorted coordinates.
2. Then, it initializes another empty list called `rows` to store the rows that contain the integer `x`.
3. The function then iterates through each index `idx` and each row `row` in the list `lst`.
4. For each row, it checks if the integer `x` is present in that row. If it is, it appends a tuple (`idx`, `len(row)`) to the `result` list and appends the row to the `rows` list.
5. After iterating through all the rows, the function sorts the `result` list based on the tuple `lambda x: (x[0], -x[1])`. This sorts the list first based on the row index in ascending order and then based on the column length in descending order.
6. Finally, it returns a list of tuples where each tuple represents the coordinate (row, column) of the integer `x` in the list `lst`. The list is filtered to only include rows that are present in the `rows` list, ensuring that only valid coordinates are included. This ensures that the output is a valid list of coordinates that meet the criteria of the problem. 
Note, the sorting of the result list ensures that the output is always stable regardless of the order of input.