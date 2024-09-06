```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 1)
 
# Test cases
assert(largest_divisor(15) == 5)
assert(largest_divisor(1025) == 25)
assert(largest_divisor(1) == 1)
assert(largest_divisor(0) == 0)
assert(largest_divisor(-14) == -14)
```
This code defines a function `largest_divisor` which aims to find the largest divisor of a given number `n`. It utilizes the `gcd` function to compute the greatest common divisor of `(n-1)` and `1`, which yields the largest divisor less than `n`.  This approach is efficient for finding the largest divisor of large numbers.