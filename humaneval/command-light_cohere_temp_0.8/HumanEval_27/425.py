```python
def flip_case(string: str) -> str:
    """
    Converts a given string where some characters are flipped between lowercase and uppercase.
    Returns the string with all characters flipped
    """
    return ''.join_(c) if c.isalpha() else c.isupper() else c.isalpha() else c else c and c == 'a' else c)

# Method Testing
def test_flipcase():
    assert flip_case('Hello') == 'olleH'
    assert flip_case('HEllO') == 'oLLo'
    assert flip_case('FOO Bar') == 'baR FOO'
    assert flip_case('abc123') == 'cAv EFg'

```