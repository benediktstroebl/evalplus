```python
def get_row(matrix, x):
    result = []
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The code works by first iterating through each element in the matrix and checking if each element is equal to the desired value `x`. When a match is found, the current index `i` and `j` are appended to the `result` list. This way, we capture the coordinates of every occurrence of `x` in the list.

After collecting all the matches, the code sorts the result based on the row index in ascending order and the column index in descending order using the `sort` method with a custom sorting key. Finally, the function returns the sorted result.