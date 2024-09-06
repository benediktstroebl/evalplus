```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        row_match = [y for y in row if y == x]
        if row_match:
            result.append((i, len(row_match)))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result
```

The `get_row` function takes two parameters: `lst`, which is a list of lists, and `x`, an integer that may or may not exist in `lst`. 

The function works as follows:
1. It initializes an empty list called `result` that will store the found coordinates.
2. It iterates over each row in `lst` using an enumerate loop.
3. Within the loop, it searches for `x` in the current row using a list comprehension, storing all the indices where `x` is found.
4. If the list comprehension finds matches, it appends a tuple `(i, len(row_match))` to the `result` list, where `i` is the current row index and `len(row_match)` is the number of occurrences of `x` in the current row.
5. Once all rows have been processed, the function sorts the `result` list first by the row index in ascending order and then by the column index in descending order (reversed order).

Finally, it returns the `result` list, which contains the coordinates of all occurrences of `x` in `lst`, sorted first by row and then by column. 

The function handles edge cases such as an empty list or a list of empty rows, returning an empty list in these cases.