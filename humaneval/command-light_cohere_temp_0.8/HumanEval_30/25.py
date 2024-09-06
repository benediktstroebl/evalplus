```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
test_get_positive = get_positive
test_get_positive([-1, 2, -4, 5, 6])
assert test_get_positive == [2, 5, 6]

test_get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_get_positive == [5, 3, 2, 3, 9, 123, 1]
```
The code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the input list. It uses a another list comprehension to iterate over the input list and check if each element is greater than or equal to zero, and if it is, it is added to the new list. The test code verifies that the function correctly.