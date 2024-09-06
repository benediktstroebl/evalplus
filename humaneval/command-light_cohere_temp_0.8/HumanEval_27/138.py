```python
def flip_case(string: str) -> str:
    return string. Flip the first letters in a given string, from lowercase to uppercase and vice versa.

def test_flip_case():
    assert flip_case("hello") == "hELLO"
    assert flip_case("world") == "WODRL"
    assert flip_case("Turn it!") == "tURIT"
    assert flip_case("to be or not") == "BNOT"
    assert flip_case("Let's do it!") == "let$Sdo$it!"
    assert flip_case("Python has a ") == "python Has a"
    assert flip_case(" COBOL ") == "co$bolL "
    assert flip_case("") is ""
```