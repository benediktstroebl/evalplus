```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be given")
    return math.isgcd(a, b)
```
Here is a Python script that contains a self-contained function that calculates the greatest common divisor of two integers a and b.

The function `greatest_common_divisor` takes two integer parameters `a` and `b` as input, and returns the greatest common divisor of a and b. The function first checks if both input parameters are not `None` and raises a `ValueError` if not. If both numbers are provided, the function then uses the `math.isgcd()` function from the time library to calculate the greatest common divisor of a and b using the `math.isgcd()` function.