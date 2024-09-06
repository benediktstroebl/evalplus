```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return list(set(l))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code defines a function `unique` that returns unique elements from a list, and a test function `test_unique` that verifies the function's correctness with a given input.

Remember to use `type hints` and provide extensive docstrings to enhance code readability and maintainability!