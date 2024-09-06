Here is a Python script that contains a self-contained function that generates a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

#Test cases
test_cases = [
    (0, "0"),
    (5, "0 5"),
    (6, "0 6"),
    (7, "0 7"),
    (8, "0 8"),
]

for n, expect in test_cases:
    actual = string_sequence(n)
    print(f"Test {n}: {actual} should be {expect}")
```