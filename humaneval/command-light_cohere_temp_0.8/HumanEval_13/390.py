```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be provided")
    return math.isgcd(a, b)
```
Here is a Python script with a self-contained function that solves the problem of finding the greatest common divisor of two numbers a and b, raising an error if the inputs are not both numbers.