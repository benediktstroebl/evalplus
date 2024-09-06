```python
def strlen(string: str) -> int:
    """ Returns length of the given string """
    return len(string)

# Test string length function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('foo bar') == 7
    assert strlen('foo-bar') == 5
    assert strlen(' ') == 1
    assert strlen(' "")" => 0
    assert strlen('123') == 3
    assert strlen('abc123') == 5    # extra trailing \n added for clarity
    assert strlen('abc\n123') == 5    # extra trailing \n for non-empty strings
    assert strlen('abc\nab') == 5    # extra trailing \n for non-empty strings with special characters

```