```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123]
```
This Python code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original input list. 

The function uses list comprehension to filter out the negative numbers from the input list. 

The code then tests the function by calling it with two different input lists and printing the resulting lists.