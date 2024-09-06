```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

def test():
    assert string_sequence(0) == '0', "String not correct!"
    assert string_sequence(1) == '1', "String not correct!"
    assert string_sequence(5) == '0 1 2 3 4 5', "String not correct!"
```