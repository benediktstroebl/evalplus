```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if char.islower() else char.swapcase() for char in string)
```

This script provides a function that takes a string as input and flips the case of its characters. The function string.swapcase() is utilized to convert lowercase characters to uppercase and uppercase characters to lowercase. This approach is employed through a generator expression in conjunction with the ''.join() function to concatenate the altered string.

To ensure functionality, execute the below code, which includes testing the function on a variety of input strings:
```python
def test_flip_case():
    assert flip_case("hello world") == "HELLO WORLD"
    assert flip_case("Hello World") == "hELLO wORLD"
    assert flip_case("ABCDEFG") == "abcdefg"
    assert flip_case("abcdefg") == "ABCDEFG"
    assert flip_case("foo BAR") == "FOO BAR"

test_flip_case()
```

Ensure that the function conforms to the expected behavior, producing the appropriate case-flipped output for each test case.