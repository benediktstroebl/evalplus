```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero")
    return abs(a - b) // gcd(a, b)

test_gcd = [
    (3, 5),
    (25, 15),
    (6, 18),
    (0, 0)
]

for a, b in test_gcd:
    print(f"Test {a} {b} - Result: {a // b}")
```