```python
def string_sequence(n: int) -> str:
    return f"0 {n} {" + str_sequence(n-1) + "}"

def str_sequence(n: int) -> str:
    if n == 0:
        return ""
    else:
        return str_sequence(n-1) + str(n)

# Unit tests
def test_string_sequence():
    assert string_sequence(0) == "0"
    assert string_sequence(1) == "1"
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(-1) == "0"
    assert string_sequence(6) == "0 6"
    assert string_sequence(10) == "0 9"
```