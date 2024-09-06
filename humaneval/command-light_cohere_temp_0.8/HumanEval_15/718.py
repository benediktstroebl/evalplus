```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2}..."
    return

# Test cases
test_cases = [
    (0, """),
    (5, "0 5 6 7 8 9"),
    (10, "0 10 10 10 10"),
    (12, "0 12 12 12 12")
]

for test_case in test_cases:
    assert string_sequence(*test_case) == test_case[1]
```