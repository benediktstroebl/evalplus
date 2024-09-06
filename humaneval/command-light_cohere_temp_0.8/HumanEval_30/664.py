```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test case 1
print(get_positive([-1, 2, -4, 5, 6]))  # Expected Output: [2, 5, 6]

#Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected Output: [5, 3, 2, 3, 9, 123]

#Test case 3
print(get_positive([-123, -232, -1]))    # Expected Output: []
```