```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Cannot find GCD of zero numbers.")
    return gcd(a, b)

# Unit tests
test_gcd = lambda: assert greatest_common_divisor(3, 5) == 1
test_gcd2 = lambda: assert greatest_common_divisor(25, 15) == 5

test_gcd3 = lambda: assert greatest_common_divisor(9, 13) == 3

# Main function execution
test_gcd()
```