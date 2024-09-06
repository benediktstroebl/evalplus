```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2}..."[n]

# test cases
test_cases = [0, 5]

for n in test_cases:
    actual_sequence = string_sequence(n)
    print(f"Test case {n}: {actual_sequence}")
```