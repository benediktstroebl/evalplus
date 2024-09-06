```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
# pass by checking that the output is correct
test_get_positive = [
    [[-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [2, 7, 6, -8]
]

assert get_positive(test_get_positive) == [2, 3, 2, 3, 9, 123, 1]

# pass another test by providing a list with only positive numbers
assert get_positive([2, 7, 6, 9]) == [2, 7, 6, 9]
```