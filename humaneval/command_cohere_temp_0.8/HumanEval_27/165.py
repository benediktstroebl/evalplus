```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as input and returns a string that flips the case of every alphabetical character. The function checks if every character in the string is alphabetical using the `isalpha()` method. If so, it uses the `swapcase()` method to change the case of every character. Otherwise, it remains unchanged, as shown in the corresponding test cases below:
```python
def test_flip_case():
    assert flip_case("Hello World") == "hELLO WORLD"
    assert flip_case("123 Hello World") == "123 hELLO WORLD"
    assert flip_case("abc def ghi") == "ABC def GHI"
    assert flip_case("abc sLjkh SAURAKJH") == "ABC sLjkh saurAKJH"
```