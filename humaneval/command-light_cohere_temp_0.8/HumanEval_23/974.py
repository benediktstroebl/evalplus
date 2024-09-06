```python
def strlen(string: str) -> int:
    return len(string)

# Test the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('123') == 3
    assert strlen('') == 0
    assert strlen('foo') == 4
```
The provided Python code defines a function `strlen` that calculates the length of a given string. It returns an integer value representing the string's length. This function is test a purpose of evaluating and passing tests to ensure its correctness. The test_strlen function contains several assertions that verify the output of the `strlen` function for various input strings.