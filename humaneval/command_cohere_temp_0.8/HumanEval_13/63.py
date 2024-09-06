```python
def greatest_common_divisor(a, b):
    """Returns the greatest common divisor of two integers a and b."""
    while b:
        a, b = b, a % b
    return a
```
The function repeatedly divides b by a, taking the remainder (a % b), and updating the divisors until b is larger than a. At each step, the value of b decreases, so the remainder (a % b) increases. This remains of b will eventually become the remainder of the initial a % b, thus ensuring that the correct value of gcd(a, b) is returned.