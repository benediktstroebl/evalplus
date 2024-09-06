```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Test cases
assert largest_divisor(15) == 5
assert largest_divisor(27) == 3
assert largest_divisor(12) == 4
assert largest_divisor(4) == 2
assert largest_divisor(2) == 1
assert largest_divisor(0) == 0
assert largest_divisor(-5) == 1
```