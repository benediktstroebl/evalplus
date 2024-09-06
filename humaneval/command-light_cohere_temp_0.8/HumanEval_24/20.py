```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, int('inf'))) + 1
 
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)
 
# Unit tests
assert(largest_divisor(15) == 5)
assert(largest_divisor(12) == 4)
assert(largest_divisor(6)==  3)
assert(largest_divisor(8) == 4)
assert(largest_divisor(20) == 5)
```