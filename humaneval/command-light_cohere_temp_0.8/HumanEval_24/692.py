```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, max(1, int)))

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

# Test cases
largest_divisor(15)  # Output: 5
largest_divisor(27) # Output: 7
largest_divisor(12) == largest_divisor(14) # True, gcd(12, 14) = 2
largest_divisor(144) # Output: 12
```