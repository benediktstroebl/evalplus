```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        cols = len(row)
        if cols == x:
            result.append((i, cols))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1])
    return result
```

The algorithm utilizes Python's `enumerate` to efficiently iterate through each `row` and its corresponding `index`. The `len` function is used to determine the `column` count for each `row`. The `result` list is populated with tuples of coordinates `(row, column)`, sorted first by row in ascending order and then by column in ascending order. This ensures the elements are neatly organized for the final output. 

The code is structured as a self-contained function, which is essential for modularity and reusability. It can handle various input scenarios, including empty lists, lists with empty rows, or rows with varying numbers of columns. It efficiently retrieves the desired row and columns and returns a list of coordinated tuples. 

This approach ensures the function is easy to maintain, adaptable, and performs the specified matrix traversal and sorting operations effectively.