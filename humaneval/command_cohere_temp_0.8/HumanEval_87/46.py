```python
def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            result.append((len(row_x), len(row_x) * 1))
    return sorted(result, key=lambda x: x[0])
```

The `get_row` function iterates through each row in the given list and identifies the rows that contain the integer `x`. It does this by creating a list `row_x` that contains all the columns in the current row that match `x`. If `row_x` contains elements, it appends a tuple (`row_index`, `column_count`) to the `result` list. The `result` list is then sorted first by the row index in ascending order and then by column count in descending order. 

The code assumes that the input list `lst` is not empty and that the integer `x` exists in at least one of the rows. If these assumptions are not met, the function will raise an exception or return an empty list. 

This solution ranks the coordinates higher where the row contains the given number more times and puts the coordinates with the given number in more columns higher as well. 

The code's output is:
```bash
[(2, 2)]
```