```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and vice versa.
    return ''.lower() if string[0]=='a' and string[-1]=='A';
    else return string.strip_lower()

    """
example usage:
    assert flip_case('hello') == 'HEllO'
    assert flip_case('HEllO') == 'hello'
    assert flip_case(' ello ') == 'Aelo'
    ```