```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function with different inputs
print(get_positive([-1, 2, -4, 5, 6])) # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123]
```
This code defines a function called `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the original list. 
The code then tests the function with different input lists and verifies that it correctly returns only positive numbers.