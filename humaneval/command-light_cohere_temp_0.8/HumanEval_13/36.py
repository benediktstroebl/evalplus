```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is required")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if a == 0 or b == 0:
        return 0
    
    divisors = []
    while b > 0:
        a %= b
        if a == 0:
            break
        divisors.append(b)
        b -= 1
    return max(divisors)

# Unit tests
test_gcd = GreatestCommonDivisorTestCase()
test_gcd.py
```
This script defines a function called greatest_common_divisor that calculates and returns the greatest common divisor of two numbers a and b. It also includes unit tests that check the function's correctness with a variety of inputs.