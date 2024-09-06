```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with various input lists
tests = [
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

for test_list in tests:
    print(get_positive(test_list))
```