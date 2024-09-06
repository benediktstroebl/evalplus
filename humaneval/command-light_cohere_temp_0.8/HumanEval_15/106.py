```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}{' ' * (n - 1)}"

# Test cases
test_cases = [
    (0, "0"),
    (1, "1"),
    (2, "0 1"),
    (5, "0 5 4 3 2 1"),
    # Add more test cases as needed
]

for n, expected in test_cases:
    actual = string_sequence(n)
    print(f"Test {n}: {actual} == {expected}")
```