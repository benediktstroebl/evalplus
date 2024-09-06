```python
def unique(lst):
    return list(set(lst))

# Test suite
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 1
test_unique()

```

This script defines a function `unique` that returns a new list with unique elements from the input list. It also includes a test suite with a simple test case that passes.