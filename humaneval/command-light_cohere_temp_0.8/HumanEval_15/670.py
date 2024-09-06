```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2} {n+3}"

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(2) == '12'
    assert string_sequence(3) == '123'
    assert string_sequence(4) == '144'
    assert string_sequence(5) == '245'
    assert string_sequence(6) == '366'
    assert string_sequence(7) == 'omalies'
    
test_string_sequence()
```