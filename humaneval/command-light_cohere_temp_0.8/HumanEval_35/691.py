```python
def max_element(lst):
    if not_unique(lst):  # Check for empty list or list with duplicates
        return None
    max_ = max(lst)
    return max

def test_max_element():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123

def test_max_element_empty():
    lst = []
    assert max_element(lst) is None

def test_max_element_invalid():
    lst = [5, 3, -5, 2, -3, 3, 9, 0]
    assert max_element(lst) is None
```
The provided code defines a Python script with a self-contained function `max_element` that solves the problem of finding the maximum element in a list. The function takes a test_max_element function tests. It creates lists with various inputs and asserts that the `max_element` function returns the correct result for each case.