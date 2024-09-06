```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test function to check the correctness of strlen
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('') == 0
    assert strlen('       ') == 5
    assert strlen('      ') == 4
```