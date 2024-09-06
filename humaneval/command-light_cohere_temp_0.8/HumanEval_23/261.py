```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns 0 if the string is empty """
    if not string: return 0
    return len(string)

# Tests
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('abcde') == 5
    assert strlen('') == 0
    assert strlen('fouro') == 5 

# Main 
if __name__ == "__main__":
    test_strlen()
```