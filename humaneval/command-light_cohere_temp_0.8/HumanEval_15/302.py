```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test cases
test_cases = [
    (0, "0"),
    (1, "1"),
    (2, "02"),
    (3, "003"),
    (4, "404"),
    (5, "0005")
]

for i, (n, expected) in enumerate(test_cases, 1):
    actual = string_sequence(n)
    assert actual == expected, f"Test case {i}: Actual {actual} != Expected {expected}"
```