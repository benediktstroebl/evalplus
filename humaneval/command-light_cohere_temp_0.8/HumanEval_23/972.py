```python
def strlen(string: str) -> int:
    return len(string)

# Test the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('') == 0
    assert strlen('     ') == 2
    assert strlen('\\t') == 3  # Contains special characters too

# Best practice for your function!
test_strlen()
```