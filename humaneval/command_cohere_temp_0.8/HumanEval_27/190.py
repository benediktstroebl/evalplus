```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)
```

This code uses a list comprehension with a conditional to determine whether each character of the input string becomes its swapped counterpart if it's in lowercase, or remains as is if it's in uppercase. Two test cases are also provided:
```python
def test_flip_case():
    assert flip_case("hello") == "HELLO"
    assert flip_case("Hello") == "hELLO"
```

To run the tests, you can call them separately:
```python
test_flip_case()
```

Or, to run them within the script, make sure to add the `if __name__ == "__main__"` block at the end of the script:
```python
def test_flip_case():
    assert flip_case("hello") == "HELLO"
    assert flip_case("Hello") == "hELLO"

if __name__ == "__main__":
    test_flip_case()
``` 

This way, when the script is executed directly, the test case functions will be invoked.