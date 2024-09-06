```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns 0 if string is empty, otherwise returns length of string"""
    if not string:
        return 0
    return len(string)

#Test suite
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('foo bar') == 7
    assert strlen('') == 0 #Should return 0
    assert len(str.split()) == 3  #Should return correct length of empty string
```