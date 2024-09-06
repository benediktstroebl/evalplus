```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

def test():
    assert string_sequence(0) == '0', "Failed with initial value"
    assert string_sequence(1) == '1', "Failed with 1"
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(6) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 10 10 10 10' # Testing above n=10
    assert len(string_sequence(10)) == 10 # Testing length of generated sequence
    test passed
```