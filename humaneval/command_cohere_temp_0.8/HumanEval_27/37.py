```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert uppercase characters to lowercase and vice versa. The condition `c.isalpha()` checks if the character is alphabetic, excluding non-alphabetic characters from the flip case conversion. Then, a list comprehension joins the characters back into a single string.

To test this code, you can use the following example:
```python
def test_flip_case():
    assert flip_case("Hello World!") == "hELLO dORL!_"
    assert flip_case("ABCDE") == "abCDE"
    assert flip_case("fooBAR") == "FOObaR"
    assert flip_case("@123") == "_1@23"
```

Overall, the code is concise and efficient in handling both alphabetical and non-alphabetical characters, effectively flipping their cases without altering the original string.