```python
def strlen(string: str) -> int:
    """ Returns length of given string"""
    return len(string)

#Test cases
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('1234') == 4
    assert strlen('') != 0
    assert strlen(' ') == 1
```