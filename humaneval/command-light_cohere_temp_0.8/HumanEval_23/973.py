Here's a self-contained Python function that calculates the length of any given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases for strlen function
test_strlen = {
    '': ()
    assert strlen('') == 0
    assert len('abc') == 3
    assert strlen('abcde') == 5
    'hello world!'[:len] == 13
    assert len('') == 0
}
```
The `strlen` function takes a string as input and returns its length.  It uses the real built-in function `len(string)` which returns the length of the string.