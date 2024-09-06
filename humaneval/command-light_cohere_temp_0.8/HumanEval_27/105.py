```python
def flip_case(string: str) -> str:
    """
    Converts a given string where characters are case-insensitive.
    -> lowercase all characters to uppercase, and vice versa
    """
    new_string = ''.join(c if c.islower() else c.isupper() else c else c else c else c.join characters to their important the result with the string.
    return new_string

def test_flip_case() -> None:
    # Test case 1
    test_string = "hello"
    assert flip_case(test_string) == "HELLO"
    # Test case 2
    test_string = "HELLo world"
    assert flip_case(test_string) == "hello world"
    # Test case 3
    test_string = "!!!!!"
    assert flip_case(test_string) == "!!!"

    return None
```