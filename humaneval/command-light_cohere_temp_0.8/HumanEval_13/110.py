```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer.")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = 25
    b = 15
    print(f"The greatest common divisor between {a} and {b} is {gcd(a, b)} = {gcd(a, b)} = 5")
```
The code defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers a and b. The function utilizes the the mathematical functions `gcd(a, b)` and `max(a, b) // gcd(a, b)` to compute the GCD. The `gcd()` function returns the minimum positive value that is a multiple of the product of `a` and `b` that is also divisible by both `a` and `b`.  The function raises a `ValueError` exception if either input is not a positive integer.