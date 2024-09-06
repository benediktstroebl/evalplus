```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test suite
def test():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert not get_positive([10, 30, 20])
    assert not get_positive([5, -5])
    assert not get_positive([])
```
This Python code defines a function `get_positive` that filters a list to include only positive numbers. It is also includes a test suite that validates the correctness of the `get_positive` function against different input scenarios.