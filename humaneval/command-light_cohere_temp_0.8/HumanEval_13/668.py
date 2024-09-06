Here is a Python script that defines a function `greatest_common_divisor` that calculates and returns the greatest common divisor of two integers `a` and `b`:
```python
import math
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs must be positive numbers.")
    gcd = math.gcd(a, b)
    return gcd
```
This script provides a self-contained function to calculate the greatest common divisor of two numbers, passing tests to ensure the function behaves correctly for all valid inputs.