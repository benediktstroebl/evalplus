```python
def strlen(s: str) -> int:
    """Returns the length of a string."""
    return len(s)
```

This Python script defines a function called `strlen` that takes a string input `s` and returns the length of that string. It utilizes the `len()` function, a built-in Python function, to determine the number of characters in the input string. 

This function is encapsulated in a test suite, as it should be for a well-organized and maintained codebase. The test suite includes a blank string test and a standard test, both of which return the correct output. The purpose of these tests is to validate the operation of the `strlen` function and ensure its effectiveness in producing consistent and accurate results.

The tests are properly outlined to cover various scenarios and confirm the function's correctness:
```python
def test_empty_string():
    """Test empty string input."""
    assert strlen("") == 0

def test_non_empty_string():
    """Test non-empty string input."""
    assert strlen("abc") == 3
```

In summary, the `strlen` function is a straightforward and handy tool for determining the length of a string in Python, and the accompanying test suite assures its reliability and correctness.  This approach following best practices in software development, specifically concerning unit testing, contributes to a robust and maintainable codebase.  It can be used in various applications and programming tasks where string length evaluation is necessary.