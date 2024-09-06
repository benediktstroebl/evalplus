```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test the function with different lists of numbers

#List with all positive numbers
print(get_positive([2, 5, 6]))  # [2, 5, 6]

# List with mix of negative and positive numbers
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123]

# List with all negative numbers
print(get_positive([-1, -2, -3, -4, -5, -6]))  # [-1, -2, -3, -4, -5, -6]
```
The function get_positive filters a list to only include positive numbers and passes those positive numbers into the return.