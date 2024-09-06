```python
def string_sequence(n: int) -> str:
    return f" {0:>{n}}"

for _ in range(10):
    assert isinstance(string_sequence(_), str), "function does not return a string"
    assert len(string_sequence(_)) == 4, "function does not return the right length"
    assert string_sequence(_) == f" {0:>{_}-{n}-{n+1}}"[:-len(f" {0:>{n}}")], "function does not return the right output")
```