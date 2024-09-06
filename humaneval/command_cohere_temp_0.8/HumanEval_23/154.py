```python
def strlen(s: str) -> int:
    """Returns the length of a string."""
    return len(s)
```

This Python script provides a function called `strlen` that takes a string as an argument and returns the string's length as an integer. The function utilizes the `len()` function, which is a built-in Python function that accepts a string as input and yields the length of that string. 

To validate the correctness of this function, two test cases are included, both of which are executed via the `pytest` testing framework. These tests are contained within a consecutively numbered marker that follows the function definition. 

The first test case, identified as `test_strlen_empty_string`, evaluates the `strlen` function on the input when the expected output is zero:
```python
def test_strlen_empty_string():
    """Test the length of an empty string."""
    result = strlen("")
    assert result == 0
```

The second test case, `test_strlen_regular_string`, assesses the `strlen` function on a regular string with content and expects the output to match the length of the string:
```python
def test_strlen_regular_string():
    """Test the length of a regular string."""
    result = strlen("abc")
    assert result == 3
```

By ensuring that these tests pass, users can have confidence in the accuracy of the `strlen` function.

```python
"""Ensure that the function behaves as intended."""
def test_strlen_empty_string():
    result = strlen("")
    assert result == 0

def test_strlen_regular_string():
    result = strlen("abc")
    assert result == 3
```
```