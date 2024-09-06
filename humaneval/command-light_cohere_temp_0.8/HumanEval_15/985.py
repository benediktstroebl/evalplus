Here is a Python script with a self-contained function that solves the problem of generating a sequence of numbers:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test cases
test_cases = [
    (0, ""),
    (5, "05021010"),
    (10, "101010101"),
    (21, "0101010101"),
]

# Test function
for n, want in test_cases:
    actual = string_sequence(n)
    assert actual == want, f"Expected {want}, got {actual}"
```
The function uses a simple mathematical formula to generate the string, and it will return the empty string at first.