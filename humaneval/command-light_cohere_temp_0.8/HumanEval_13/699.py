```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return math.isgcd(min(a, b))
```
In this code, the greatest_common_divisor function calculates the greatest common divisor of two numbers using the math.py.mathdef (built- library's `math` module). This is a standard method to find the greatest common divisor of two integers.