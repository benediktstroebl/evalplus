```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive approach is quite efficient:
- The base case occurs when b is 0, where the GCD is obviously a.
- In general, the GCD of a and b will be the same as the GCD of b and a % b, where % is the modulo operator. 

This is based on the principle that dividends and divisors come in pairs. If d is a common divisor of a and b, then a = pd and b = qd for some integers p and q. Substituting into the second expression for the GCD, we get:
GCD(b, a % b) = GCD(b, (p % d)d) = GCD(b, p % d)
since b/d and (p%d)d have the same remainder when divided by d. 

Since the GCD of b and p%d must be a common divisor of b and a, the recursive approach works.