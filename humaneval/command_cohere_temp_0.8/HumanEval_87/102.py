```python
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The `get_row` function iterates through each nested list within the input list `lst`, and for each nested list, it iterates through each element. When it finds an element equal to the target integer `x`, it creates a tuple (`i`, `j`) representing the current index `i` and column index `j`. This tuple is appended to the `result` list.

After finding all the matches, the function sorts the `result` list based on the tuple's elements. The first element is sorted in ascending order representing the row index, and the second element is sorted in descending order representing the column index. 

This sorting ensures that the resulting list of tuples is organized in a consistent format. The example usage and test cases accurately represent the problem's requirements, and the function properly handles edge cases.  The code is efficient and accurately solves the problem.