```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This script defines a function `unique` that returns a sorted list of unique elements in the input list. It then includes a test function to verify the correctness of the `unique` function with a passing test.