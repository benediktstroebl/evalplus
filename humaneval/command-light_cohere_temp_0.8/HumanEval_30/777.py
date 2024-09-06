```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with different input
print(get_positive([-1, 2, -4, 5, 6]))  # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123]

```
This Python function, get_positive, takes a list as input and returns a new list containing only the positive numbers from the input list. It uses list comprehension to filter out the numbers that are greater than zero.