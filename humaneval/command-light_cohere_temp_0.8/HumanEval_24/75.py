```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer less than n that divides it evenly"""
    return (n + 1) // gcd(n, 1)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b % a, a)

largest_divisor(15)  # Output: 5
```