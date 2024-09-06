```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
# Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3 (Alternatively: [0, -1, 2, 3, 4, 5, 6])
print(get_positive([0, -1, 2, 3, 4, 5, 6]))
# Expected output: [0, -1, 2, 3, 4, 5, 6]
```
This Python function, `get_positive`, takes a list as input and returns a new list with only the positive numbers from the original input list. It uses list comprehension to iterate through each element in the input list and checks if the number is non-negative, in which case it is positive. The resulting list will only contain elements that are greater than or equal to zero.