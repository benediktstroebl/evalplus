```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence():
    assert string_sequence(0) == '0', "0 should be 0"
    assert string_sequence(1) == '1', "1 should be 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Output should be 012345"
    assert string_sequence(10) == '9Increment9', "n should increment"
    assert string_sequence(20) == '89989889', "n should increment even more"
    
# Call test_string_sequence function
test_string_sequence()
```