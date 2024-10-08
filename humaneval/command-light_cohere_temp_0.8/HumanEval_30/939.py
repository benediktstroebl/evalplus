```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test cases
print(get_positive([-1, 2, -4, 5, 6]))        # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123, 1]
```
This code defines a function, `get_positive`, which takes a list as input and returns a new list containing only the positive numbers from the original list. The function uses a specific list comprehension to achieve this and uses the condition `num > 0` to filter out the positive numbers.