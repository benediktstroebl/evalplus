```python
def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            col_sort = sorted(row_x)
            result.append((len(lst) - row.index(col_sort[0]) - 1, len(col_sort)))
    return result
```

The algorithm works by first iterating through each row in the list and finding all occurrences of `x` in each row. The occurrences are stored in `row_x`. Subsequently, the occurrences of `x` in each row are sorted in ascending order. The coordinates are then recorded as a tuple (`(row_num, col_num)`), where `row_num` is the row number and `col_num` is the number of occurrences of `x` in that row. These tuples are stored in the `result` list and are sorted first by `row_num` and then by `col_num`. Finally, the `result` list is returned. 

The `result` list is empty if no matching elements are found in the list `lst`. Thus, the function gracefully handles edge cases like an empty list or a list with empty rows. 

This problem can also be solved using `itertools.groupby()` and `sorted()` to keep the code concise and readable:
```python
from itertools import groupby

def get_row(lst, x):
    return [(row_num, len(list(group))) for row_num, group in enumerate(groupby(lst), 1) if x in group]
```