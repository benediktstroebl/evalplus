```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function with different values of n
test_sequence = [
    (0, '0'),
    (5, '050105'),
    (10, '010101010'),
    (100000, '10000000000')
]

for n, expected in test_sequence:
    actual = string_sequence(n)
    print(f"Test {n}: {actual} => {expected}")
```