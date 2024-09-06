```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} all {n+3}"

#Test cases
test_sequence = [
    (0),
    (5),
    (12345),
    (123456789),
]

for i, n in enumerate(test_sequence):
    assert string_sequence(n) == f"0 {n} {n+1} {n+2} all {n+3}", f"Test passed: {i+1}"
```