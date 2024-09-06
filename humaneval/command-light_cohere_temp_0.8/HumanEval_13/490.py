```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    # Use formula to find GCD
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)

# Test cases
test_gcd = [
    (3, 5),
    (25, 15),
    (128, 64),
    (0, 0),
    (9, 27),
    (21, 13),
]

for test in test_gcd:
    print(f"Test {test[0]}: {test[1]} GCD:", greatest_common_divisor(test[0], test[1]))
```