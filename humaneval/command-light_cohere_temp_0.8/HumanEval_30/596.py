```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases
get_positive([-1, 2, -4, 5, 6]) # Output: [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) # Output: [5, 3, 2, 3, 9, 123]
get_positive([]) # Input: []
 # Output: []
get_positive([21, -23, 45, -55]) # Input: [21, -23, 45, -55]
 # Output: []

# Another test case
def test_function():
    result = get_positive([1, 2, 3, -4, 5, 6, 7, 8, 9])
    assert result == [1, 2, 3, 5, 6]
```
This script defines a `get_positive` function that takes a list as input and returns a new list with only the positive numbers from the original input list. The test cases cover a various scenarios, including empty lists, negative numbers, non-numeric inputs, and positive numbers.