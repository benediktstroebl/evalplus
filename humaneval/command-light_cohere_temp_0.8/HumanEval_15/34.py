```python
def string_sequence(n: int) -> str:
    return f" {0:0b}".join(n)

def test_sequence(n: int, expected: str) -> None:
    assert string_sequence(n) == expected, f" {n} != {expected}"

# Run tests
test_sequence(5, '0 1 2 3 4 5')
test_sequence(0, '0')
```