```python
def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if cols == x:
            result.append((len(lst) - row[::-1].index(row), cols))
    return sorted(result, key=lambda x: (x[0], -x[1]))
```

The function iterates through each row in the list and determines whether the number of columns in a current row is equal to the given x. When these conditions are met, a tuple is created and appended to the result list, which is subsequently sorted in the required order. The first element of the tuple is the row number, determined by counting the number of rows and reversing the row to find the column's position, while the second element is the column number. The final result is returned once all rows have been processed.

Here is an example of how you can use the function with a test:
```python
test = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 1, 6],
    [1, 2, 3, 4, 5, 1],
]

x = 1
expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

assert get_row(test, x) == expected
```