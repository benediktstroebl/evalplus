```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1,  9)
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
``` 
This code defines a function `largest_divisor(n)` that calculates the largest number that evenly divides `n`. It uses the `gcd()` function to calculate the greatest common divisor of `n - 1` and 9.