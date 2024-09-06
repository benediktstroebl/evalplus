Here is a Python script that contains a self-contained function that solves the problem of returning unique elements in a list:
```python
def unique(lst):
    """Return unique and sorted elements in a list"""
    uniq = list(set(lst))
    return sorted(uniq)

# Tests
def test_unique():
    list1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [0, 2, 3, 5, 9, 123]
    actual = unique(list1)
    assert expected == actual
```
This script defines a function unique that returns a list of unique and sorted elements in the input list. The function is then tested using a test function test_unique that creates a list and checks if the returned unique elements are correct.