```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Testing the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('') == 0  # Should return 0
```