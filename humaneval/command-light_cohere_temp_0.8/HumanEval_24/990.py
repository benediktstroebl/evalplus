```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, -1)
def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x
# Unit tests
n = 15
assert largest_divisor(n) == 5
``` 
This code provides a function `largest_divisor` that calculates the largest number which divides a given number `n` evenly, and a helper function `gcd` that computes the greatest common divisor of two numbers. The function also provides a tests to ensure the function is correct.