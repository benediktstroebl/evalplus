```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123]

# Test case 3
print(get_positive([]))  # Expected output: []

# Test case 4
print(get_positive([1, 2, 3, -1, -4]))  # Expected output: [1, 2, 3]
```
This Python code defines a function called **get_positive** that takes a list as input and returns a new list containing only the positive numbers from the original list. It uses list comprehension and simple conditional statements to filter out the positive numbers.