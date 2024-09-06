```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be non-zero")
    return math.gcd(a, b)
``` 
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function uses the built-in `math.gcd()` function to calculate the greatest common divisor of two numbers.