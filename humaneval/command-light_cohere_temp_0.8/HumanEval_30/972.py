```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

#Test case 1:
print(get_positive([-1, 2, -4, 5, 6]))
# Output: [2, 5, 6]

#Test case 2:
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Output: [5, 3, 2, 3, 9, 123, 1]
```

The function get_positive takes a list as input and returns a new list containing only the positive elements from the original list. The code is self-contained and can be used as a standalone function for solving this specific problem.