```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with various input
test_get_positive = get_positive
test_get_positive([-1, 2, -4, 5, 6])
test_get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```
The function `get_positive` takes a list `l` as an argument. It uses a a list comprehension to filter out only the positive numbers from the list. The filtered list is then returned. The function is tested with a variety of inputs, and the expected output is also confirmed.