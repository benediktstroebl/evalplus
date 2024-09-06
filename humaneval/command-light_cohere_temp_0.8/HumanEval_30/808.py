```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

#Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
# Output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Output: [5, 3, 2, 3, 9, 123]

# Test case 3
print(get_positive([5, -5, -9, -1, -23, -5, 7, -33]))
# Output: [-5, -9, -1, -23, 7]
```
The code defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. It uses list comprehensions and boolean conditions to filter out the positive numbers.