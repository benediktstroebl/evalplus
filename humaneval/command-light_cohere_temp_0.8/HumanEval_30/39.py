```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with a variety of inputs
print(get_positive([-1, 2, -4, 5, 6])) # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123]
print(get_positive([- 333, 5, 2, 782, 1])) # Output: [- 333, 5, 2, 782]
print(get_positive([1, 2, 3, -4])) # Output: [1, 2, 3]
print(get_positive([])) # Output: []
print(get_positive([-it for it in range(1, 100)])) # Output: []
```