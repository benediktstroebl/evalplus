```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

for _ in range(10):
    assert string_sequence(11) == '0 11 12 13 14 15 16 17 18 19 20', 'Test failed!'
    assert string_sequence(0) == '0', 'Test failed!'
```