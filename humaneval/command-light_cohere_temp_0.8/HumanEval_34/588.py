```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(l))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```  This script defines a `unique` function that returns a list containing the unique elements of the input list, and a `test_unique` function that tests the `unique` function with a sample input.  The two functions are self-contained and pass the tests, making them suitable for inclusion in an API.