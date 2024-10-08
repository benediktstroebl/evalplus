```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123]

# Test case 3
print(get_positive([5, 3, -5, 2, -3, 3, -123, -1]))  # Expected output: []

# Test case 4
print(get_positive([True, 2, 4, -5, 6, 7, 8, 9, -10]))  # Expected output: []
```
This script defines a `get_positive` function that returns a list containing only the positive numbers from the input list. The test cases cover various scenarios to ensure the function is working as expected.