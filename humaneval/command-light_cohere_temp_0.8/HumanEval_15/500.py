```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n inclusive"""
    return f"0 {n} {" + string_sequence(n - 1) + "}"

def test_string_sequence(n: int) -> None:
    assert string_sequence(n) == f"0 {n} {}", "Test failed: wrong sequence returned"
    assert string_sequence(n - 1) == "0 ", "Test failed: wrong initial value"
    assert len(string_sequence(0)) == 1, "Test failed: empty sequence"
    assert string_sequence(7) == "0 7 8 9", "Test failed: wrong sequence returned"

# Example usage
test_string_sequence(7)
```