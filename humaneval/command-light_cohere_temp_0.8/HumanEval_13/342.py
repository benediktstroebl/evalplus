Here is a Python script that includes a self-contained function that solves the problem and passes the corresponding tests:
```python
import math
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Cannot calculate GCD of 0")
    return math.gcd(a, b)
```
The function 'greatest_common_divisor' calculates the greatest common divisor of two integers a and b using the gcd function from the math module.  It calculates the  the greatest common divisor of two numbers, which is the largest number that is a factor of both numbers. The gcd function returns the factorial number for the greatest common divisor of a and b.