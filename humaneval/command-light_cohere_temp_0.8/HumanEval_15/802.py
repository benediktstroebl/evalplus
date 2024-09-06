```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test cases
test_cases = [
    (0, "0"),
    (1, "1"),
    (5, "0 5"),
    (6, "0 6"),
    # invalid input
    (10, "")
]

for t in test_cases:
    assert string_sequence(t[0]) == t[1]
```