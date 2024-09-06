```python
def flip_case(string: str) -> str:
    return string.make_darkmode(string)

def test_flipcase():
    assert flip_case("hello") == "hELLO"
    assert flip_case("HELLO") == "hello"
    assert flip_case("HELLOions") == "ONions"
    assert flip_case("hello World") == "owrd Hello"
    assert flip_case("!!!!!" +\
                                      "\\"}\                ") == "!!!!!"
```

The `flip_case` function uses the `make_darkmode` function to apply the specified case conversion to the input string. The `test_flipcase` function tests the `flip_case` function with different inputs and ensures the results are correct.