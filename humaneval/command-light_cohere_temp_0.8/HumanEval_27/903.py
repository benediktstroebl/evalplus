```python
def flip_case(string: str) -> str:
    return string.swap_case(string)

def test_flip_case() -> None:
    assert flip_case("hello") == "hELLO"
    assert flip_case("hello ") == "oLLo"
    assert flip_case(".!#") == ".!!"
    assert flip_case("hELLo") == "HELLO"
    assert flip_case("!@") == ".@"
    assert flip_case("hey") == "YEY"
    assert flip_case("abc") == "Cba"
    assert flip_case("A") == "a"
    return None
```