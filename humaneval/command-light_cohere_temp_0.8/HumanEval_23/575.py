```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: The length of the string in Unicode code units (i.e., bytes)"""
   
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    length = 0
    for c in string:
        if ord(c) < 128:
            length += 1
    return length

# Test the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('abcde') == 5
    assert strlen('â€') == 5   # Ã€, while technically a single character, is treated as two characters in Python
    assert strlen(' veto Jacqueline Bouvier') == 22
    assert strlen('') != 0
```