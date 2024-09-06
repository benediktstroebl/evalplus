```python
def flip_case(string: str) -> str:
    return string.flip()
def test_flip_case():
    assert flip_case("Hello") == "HEmLLo", " failing test case"
    assert flip_case("hello") == "HEllO", " failing test case"
    assert flip_case("ALLl inline with all uppercase") == "aLLll ínline uP UppErCasE"
    return
test_flip_case()
```