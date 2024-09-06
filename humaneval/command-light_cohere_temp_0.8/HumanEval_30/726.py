```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with different lists
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]

# Negative test cases
print(get_positive([-7, -8, -9, -10]))  # Expected output: []
print(get_positive([9, 2, 3, -20]))  # Expected output: [9, 2, 3]

# Test with a string
print(get_positive("Hello"))  # Expected output: []
```