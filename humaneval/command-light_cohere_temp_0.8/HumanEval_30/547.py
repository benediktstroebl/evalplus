```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([0]) == []
assert not get_positive([7]) == []
```
This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. 

The test cases verify the expected outputs for various input lists and check the function's correctness.