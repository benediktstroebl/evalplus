Here is a Python script that includes the function `greatest_common_divisor`, which calculates the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Returns the greatest common divisor of a and b."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both 'a' and 'b' must be integers")
    if a == 0 or b == 0:
        return 0
    gcd = __import__('math').gcd(a, b)
    return gcd
```

This script defines a function `greatest_common_divisor` that calculates the greatest common divisor between two integers `a` and `b`. It uses Python's built-in function `gcd` to calculate the greatest common divisor, and includes input and type checks to ensure valid input.