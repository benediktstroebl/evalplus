```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, int('inf'))

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Unit tests
assert(largest_divisor(6) == 3)
assert(largest_divisor(10) == 5)
assert(largest_divisor(20) == 5)
assert(largest_divisor(25) == 5)
assert(largest_divisor(30) == 5)
assert(largest_divisor(15) == 5)
assert(largest_divisor(12) == 4)
assert(largest_divisor(27) == 3)
```
This code implements a function **largest_divisor** that takes an integer n as input and returns the largest integer that evenly divides n, ensuring that it is less than n. The function uses the GCD to find the greatest common divisor of n - 1 and inf. This value, combined with n - 1, provides the largest number that divides n evenly.