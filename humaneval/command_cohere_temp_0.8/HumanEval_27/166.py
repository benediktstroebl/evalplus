```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() for char in string)
```
The function utilizes the `swapcase` method to effectively reverse the case of each character in the string. This is a more concise approach compared to manually toggling cases using conditional statements. Thus, the script achieves the desired outcome of flipping the case while maintaining good readability and efficiency.

Here is a test case to test the function:
```python
def test_flip_case():
    assert flip_case("hello World") == "HELLO world"
    assert flip_case("ABCDE") == "abCDE"
    assert flip_case("abcde") == "Abcde"
    assert flip_case("123") == "321"
    assert flip_case("foo BAR") == "FOO bar"
``` 
This test case covers different types of characters that require case flipping.