```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return max(a, b) / gcd(a, b)
 
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
 
# Unit tests
assert(greatest_common_divisor(3, 5) == 1)
assert(greatest_common_divisor(25, 15) == 5)
```
This code defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. The function also implements a helper function, `gcd(a, b)`, which computes the greatest common divisor of two numbers `a` and `b`. The `gcd` function uses the Euclidean algorithm to find the greatest common divisor efficiently. Finally, the tests the use the code to ensure the function works correctly.