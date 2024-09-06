```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function
test_get_positive = get_positive

print(test_get_positive([-1, 2, -4, 5, 6])) # Expected output: [2, 5, 6]
print(test_get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Expected output: [5, 3, 2, 3, 9, 123, 1]
```
This script defines a function `get_positive` that takes a list as input and returns a new list with only the positive numbers from the original list. The test cases pass successfully, demonstrating that the function works as expected.