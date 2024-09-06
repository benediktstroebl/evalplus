```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

#Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
assert not get_positive([0])
assert not get_positive([-n for n in range(1000)])
```  This script defines a `get_positive` function that takes a list as an argument and returns a new list containing only the positive numbers from the original list. 

The `assert` statements are used to test the correctness of the `get_positive` function with various input lists, and ensure that it returns the expected output.