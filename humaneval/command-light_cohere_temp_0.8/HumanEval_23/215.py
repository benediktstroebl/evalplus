```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns 0 if the string is empty """
    if not string: return 0
    return len(string)

# Test function to check the implementation
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('foo bar') == 7
    assert strlen('') == 0
```
The provided code defines a function `strlen` that calculates the length of a given string. It returns 0 if the The string is empty, otherwise, it returns the length of the string using the `len()` function. The `test_strlen` function is used to check the correctness of `strlen` function.