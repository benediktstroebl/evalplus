```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(2) == '01'
    assert string_sequence(3) == '001'
    assert string_sequence(4) == '010'
    assert string_sequence(5) == '050'
    assert string_sequence(6) == '0600'
    assert string_sequence(7) == '0700'
    assert string_sequence(8) == '0800'
    assert string_sequence(9) == '0900'

# Run the above test function to ensure the function works correctly
test_sequence()
```