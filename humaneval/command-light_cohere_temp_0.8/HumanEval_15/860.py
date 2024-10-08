```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str(n) + "}" * (n + 1)

def test_string_sequence():
    assert str(string_sequence(0)) == '0', "Test 1 failed"
    assert str(string_sequence(5)) == '0 1 2 3 4 5', "Test 2 failed"
    assert str(string_sequence(10)) == "000 10 10 10 10", "Test 3 failed"
    return "All tests passed"
```