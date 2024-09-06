```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence():
    assert str(string_sequence(0)) == '0', "Test case 0 failed"
    assert str(string_sequence(1)) == '1', "Test case 1 failed"
    assert str(string_sequence(5)) == '0 1 2 3 4 5', "Test case 5 failed"
    assert str(string_sequence(10)) == '0 10 11 12 13 14', "Test case 10 failed"
    assert len(string_sequence(5)) == 10, "Length of sequence is not 10"
```