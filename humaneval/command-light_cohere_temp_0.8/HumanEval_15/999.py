```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence():
    assert str(string_sequence(0)) == '0', "Should start with 0"
    assert str(string_sequence(1)) == '1', "Should add 1"
    assert str(string_sequence(5)) == '0 1 2 3 4 5', "Should reach 5"
    assert str(string_sequence(10)) == '0 9 8 7 6 5 4 3 2 1', "Should reach 10"
    assert str(string_sequence(1000000)) == '0 1 999 998 997 999 98', "Should reach 1000000"
```