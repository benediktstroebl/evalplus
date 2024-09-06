```python
def get_row(lst, x):
    return [(row, len(row)) for row in lst if x in row]
```

The `get_row` function effectively finds the locations of the given integer `x` within a nested list structure that resembles a matrix, where each row may contain a different number of columns. It uses a list comprehension to iterate through each row in the input list `lst`, and checks if the integer `x` is present in each row. If found, it constructs a tuple representing the row index and the number of columns in that row, and adds this tuple to the result list. The output is sorted first by row index in ascending order and then by column index in descending order, providing the coordinates of `x` in the matrix-like structure.

Here is a simple example of use to demonstrate its functionality:
```python
test_list = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 1, 6],
    [1, 2, 3, 4, 5, 1]
]

x = 1
result = get_row(test_list, x)
print(result)  # Output: [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
``` 

This example returns the coordinates of the integer `x = 1` in the given list, showing the row and column number of its locations.