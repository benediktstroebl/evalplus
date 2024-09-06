```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function
def test_get_positive():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = [5, 3, 2, 3, 9, 123, 1]
    got = get_positive(test_list)
    assert expected == got
```