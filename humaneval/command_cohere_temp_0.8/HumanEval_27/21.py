```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. The `swapcase` method is used for the flipping, whereas non-alphabetical characters like spaces are left unchanged. 

To properly test this function, one would need to verify that it correctly flips a mix of uppercase and lowercase characters, as well as ensure that non-alphabetical characters remain the same. Here is an example of a test: 

```python
def test_flip_case():
    assert flip_case("hElLo") == "HeLLo"
    assert flip_case("JeNe Parlerai en Francais") == "jENe pArLeReAI en fRaNcAIS"
    assert flip_case("ABC$%^&*()") == "aBC$%^&*()"
    assert flip_case("multiple words") == "multiple WORDS"
    assert flip_case("hello world") == "HELLO world"
``` 

The test code snippet provided checks the function's behavior on a diverse range of inputs, ensuring that each character is correctly flipped while non-alphabetical characters remain unchanged.