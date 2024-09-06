```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123])
assertEqual(get_positive([]), [])
assertEqual(get_positive([None, 1, 2]), [1, 2])

# This would throw an error without float_cmp module installed
try:
    assert get_positive([1.2, 2..1, 1]) is raise ValueError: 'Different types in comparison'
```