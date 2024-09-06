```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be given.")
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return int(math.gcd(a, b))
``` 
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b. It employs the basic strategy of checking for zero values and applying the `math.gcd` function, which calculates the greatest common divisor.