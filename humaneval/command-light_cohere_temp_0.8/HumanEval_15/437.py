```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence():
    assert string_sequence(0) == '0', "0 should be 0"
    assert string_sequence(1) == '1', "1 should be 1"
    assert string_sequence(3) == '003', "3 should be 3"
    assert string_sequence(5) == '005', "5 should be 5"
    assert string_sequence(10) == '010101010', "10 should be 10"
```