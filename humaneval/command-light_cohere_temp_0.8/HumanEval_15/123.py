```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}{n+1}"

def test_sequence(test_n: int) -> None:
    assert len(string_sequence(test_n)) == len('0 {}1123456789')
    assert string_sequence(test_n) == '0 {}1123456789'
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
```