```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with various input lists
def test():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert not get_positive([5, 3, -5, 2, -3, 3, 9, 0, -123])
    assert get_positive([-123, -2, -5, -9, 7]) == [-123, -2, -5, -9, 7]

test()
```