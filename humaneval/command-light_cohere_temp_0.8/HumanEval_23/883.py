```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Tests
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('') == 0  # empty string

if __name__ == "__main__":
    test_strlen()
```
This script defines a function `strlen` that calculates the length of a given string. It also includes a test function that verifies the correctness of the `strlen` function with various inputs.