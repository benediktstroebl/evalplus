```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a string that flips the case of every letter. It uses the swapcase function on alphabetic characters and leaves non-alphabetic characters unchanged. Test cases can be added to ensure the function works correctly. For example, adding the test case below confirms that the function flips the case of all letters in the string:
```python
def test_flip_case():
    assert flip_case("hEyEz_20bIg") == "HEyEz_2bIg"
```