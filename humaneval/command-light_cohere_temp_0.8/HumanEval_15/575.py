```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2} {n+3}"

def test_string_sequence():
    assert str(string_sequence(5)) == '0 5 6 7 8', "Failed: Test string_sequence returned unexpected output"
```