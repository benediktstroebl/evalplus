```python
def flip_case(string: str) -> str:
    return string.flip()

def test_flip_case()():
    assert flip_case("hello") == "hELLO"
    assert flip_case("HELLO") == "hello"
    assert flip_case("hello World!") == "hELLO World!"
    assert flip_case("A") == "a"
    assert flip_case("aa") == "Aa"
    assert flip_case("ABC") == "CBM"
    assert flip_case("123") == "123"
```