```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```
This code defines a function called `get_positive` that takes in a list as an argument. The function returns a a list of only the positive numbers from the original list. 

This code is self-contained and does not use any external functions or modules, which is a good practice for creating small, reusable utility functions.