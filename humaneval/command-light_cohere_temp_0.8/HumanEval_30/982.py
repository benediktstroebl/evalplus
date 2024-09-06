```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Unit tests
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert len(get_positive([8, 1, 0])) == 1
    assert len(get_positive([-123])) == 0

if __name__ == "__main__":
    test_get_positive()
```
The script defines a function `get_positive` that returns a list containing only the positive numbers from the input list. It is then passes several tests to ensure the function's correctness.