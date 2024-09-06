```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    return max(gcd(a, b), 1)

def gcd(a, b):
    while b:
        a, b = b, a % b

# Unit tests
test_gcd = lambda: greatest_common_divisor(5, 15)  # Expected: 1
test_gcd2 = lambda: greatest_common_divisor(3, 125)  # Expected: 5
test_gcd3 = lambda: greatest_common_divisor(10, 2)  # Expected: 2
test_gcd4 = lambda: greatest_common_divisor(-5, 10)  # Expected: ValueError: Both numbers must be positive
```