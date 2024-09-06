```python
def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    cols = []
    for row in lst:
        cols.append(len(row))
    for i, r_cols in enumerate(cols):
        if r_cols == x:
            result.append((i, r_cols))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The `get_row` function takes in two parameters: `lst`, which is an arbitrary nested list, and `x`, an integer representing the desired column count. 

This function works in the following way:
1. First, it initializes an empty list called `result` to store the final output.
2. It creates another list called `rows` to store the row indices that contain `x` columns. This is achieved using the list comprehension `[len(row) for row in lst]`.
3. Next, it creates another list called `cols` where each element represents the column count of the respective row. This is achieved by iterating over each row in `lst` and appending its column count.
4. Afterwards, it iterates through each element in `cols` and checks if it matches `x`. If it does, it constructs a tuple `(i, r_cols)` where `i` is the row index, and `r_cols` is the column count. This tuple is then appended to `result`.
5. Finally, all tuples are sorted first by the row index in ascending order and then by the column count in descending order, ensuring that the output is always sorted in the same manner. 

The function returns the `result` list of tuples.