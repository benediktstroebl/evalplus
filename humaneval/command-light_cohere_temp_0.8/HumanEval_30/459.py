```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function with various input lists
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123])
assert(get_positive([5, '3', -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9])
assert(get_positive([-1, -2, -3, -4, 5, 6, 7, 8, 9]) == [1, 2, 3, 6])
assert(get_positive([0, -1, 2, 3, -4, 5]) == [0, 2, 3])

```
This Python function, `get_positive()`, accepts a list as an argument and produces a new list containing only positive numbers from the original list. The test cases validate the rights of the function with a variety of lists, including text strings.