```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with various input
# Should return the following:
# [2, 5, 6]
# [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
# [5, 7, 2, 4, -8, -6]
# [5, 5, 5]
# [6, 2, -6]

test_positive = [1, 2, -4, 5, 6, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(test_positive))
```