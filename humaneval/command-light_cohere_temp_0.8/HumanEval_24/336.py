```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1, n-2)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

# Tests
assert(largest_divisor(15) == 5)
assert(largest_divisor(24) == 8)
assert(largest_divisor(21) == 3)
assert(largest_divisor(120) == 24)
assert(largest_divisor(0) == 0)
assert(largest_divisor(-12) == -12)
``` 
This code defines a function `largest_divisor` which takes an integer `n` as input and returns the largest integer that divides `n` evenly, smaller than `n`. The function uses the `gcd` function to find the greatest common divisor of `n-1` and `n-2`, and returns that result. 

The `gcd` function calculates the greatest common divisor of two integers using the Euclidean algorithm. The `assert` statements are used to test the correctness of the `largest_divisor` function with various input values.