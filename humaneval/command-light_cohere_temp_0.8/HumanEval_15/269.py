```python
def string_sequence(n: int) -> str:
    return f" {0:>{n}} "
for i in range(1, n+1):
    assert str(string_sequence(i)) == f" {i:>{n}} ", f"{i} must be a valid sequence"
    return string_sequence(n)
```