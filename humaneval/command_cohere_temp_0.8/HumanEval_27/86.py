```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that takes a string as an input and returns a string with flipped cases for every character, leaving non-alphabetic characters unchanged. Case swapping is performed using the `swapcase()` method. This solution ensures that punctuation and other non-alphabetic characters remain the same, while alphabetic characters have their case flipped. 

To verify the functionality, you can run tests using the following script:
```python
def test_flip_case():
    assert flip_case("Hello World") == "hELLO WORLD"
    assert flip_case("SQLite") == "sQLITE"
    assert flip_case("python") == "PythOn"
    assert flip_case("2.14.2") == "2.14.2"
    assert flip_case("AStringWithNonAlphabeticCharactersABC") == "aStringWithNonAlphabeticCharactersabc"

test_flip_case()
```

Adjust the test script according to your needs or use it to verify the functionality of the `flip_case` function.