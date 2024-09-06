```python
def unique(lst):
    return list(set(lst))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
The code defines a function `unique` that returns a list of unique elements from the input list `lst` using the `set()` function and the `list` constructor. The `test_unique` function tests the list with various inputs and ensures that the `unique` function returns the expected result.