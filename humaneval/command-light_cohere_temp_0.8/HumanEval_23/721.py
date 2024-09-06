```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

#Test case 1
def test_strlen():
    assert strlen('') == 0

#Test case 2
def test_strlen2():
    assert strlen('abc') == 3
```

This script defines a function `strlen` that calculates the length of a given string. It is then tested using two different test cases.