```python
def string_sequence(n: int) -> str:
    return f" {0:>{n}"
    return f"_{n}" * (n+1)

def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(3) == '003'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '00010101'
    assert string_sequence(100) == '01001000010'
```