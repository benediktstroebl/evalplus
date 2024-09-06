```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test case 1: Should return [2, 5, 6]
print(get_positive([-1, 2, -4, 5, 6]))

# Test case 2: Single element list
print(get_positive([5]))

# Test case 3: Empty list
print(get_positive([]))

# Test case 4: List with negative number
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
This code defines the `get_positive` function, which takes an input list and returns a new list containing only the positive elements from the original list. The test cases are an way to validate the correctness of this function.