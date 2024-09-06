```python
def flip_case(string: str) -> str:
    return string. flipcase()

def test_flip_case():
    assert flip_case("hello") == "HELLO"
    assert flip_case("HELLO") == "hello"
    assert flip_case("HELLOivated!") == "oIVatedH"
    assert flip_case("HELLoXXX") == "xlloHH"
```