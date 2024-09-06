```python
def strlen(string: str) -> int:
    return len(string)

# Test the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('123') == 3
    assert strlen('     ') == 3
    assert strlen('abc123') == 7
    assert strlen('abc\ndc') == 7
    assert strlen('abc123_') == 7
```