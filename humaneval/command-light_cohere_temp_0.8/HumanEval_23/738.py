```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Tests
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('') == 0
    assert strlen('1234') == 4


# Main method
if __name__ == "__main__":
    test_strlen()
```
This script defines a function `strlen` that calculates the length of a given string. The function returns an integer value representing the length. The test suite ensures the correctness of the `strlen` function by passing various test cases.