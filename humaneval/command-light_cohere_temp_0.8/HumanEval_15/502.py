```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

def test_string_sequence():
    assert string_sequence(0) == '0', "Failed test for string_sequence(0)"
    assert string_sequence(1) == '1', "Failed test for string_sequence(1)"
    assert string_sequence(5) == '0 5', "Failed test for string_sequence(5)"
```
Do you want me to assist you in writing any other Python-related code or assist with another idea you want to bring up?