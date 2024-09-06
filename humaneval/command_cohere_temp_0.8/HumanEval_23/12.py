```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```

This Python script provides a function termed `strlen` taking a string argument and returning its length. The function utilizes the built-in Python `len()` method to determine the length of the given string. It is a self-contained code block demonstrating the `strlen` function's usefulness in calculating string lengths.

Here is an example of how to use the `strlen` function:
```python
def test_strlen():
    """ Tests for the strlen function """
    assert strlen("Hello, World!") == 13
    assert strlen("") == 0
    assert strlen("abcdefghijklmnopqrstuvwxyz") == 26
    assert strlen("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 52
```

This section includes a test suite with four assertions to validate the behavior of the `strlen` function. These tests cover a range of scenarios, including empty strings, standard strings, and uppercase strings, to ensure the function's correctness in returning the string length.