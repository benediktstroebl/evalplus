```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

def test():
    assert str(string_sequence(0)) == '0', "Failed Test 0"
    assert str(string_sequence(1)) == '1', "Failed Test 1"
    assert str(string_sequence(5)) == '0 1 2 3 4 5', "Failed Test 2"
    return "OK"
```