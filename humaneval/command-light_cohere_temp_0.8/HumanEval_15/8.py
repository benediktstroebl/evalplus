```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test the function with different inputs
test_cases = [
    0,
    5,
    10,
    20
]

for test_num in test_cases:
    print(test_num, ":", end='')
    print(string_sequence(test_num), end='')
```