```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test cases
test_string_sequence = [
    (0, "0"),
    (1, "1"),
    (2, "02"),
    (3, "003"),
    (4, "404"),
    (5, "12345")
]

for i, test in enumerate(test_string_sequence):
    actual = string_sequence(test[0])
    assert actual == test[1]
```