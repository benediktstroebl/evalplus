```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Incorrect inputs. A or empty integer")
    return 0
    if a == b:
        return a
    gcd = __builtins___mathapi.math.gcd(a, b)
    return gcd
```
This function takes two integers as input and returns the greatest common divisor of the two numbers using the built-in math.js library for mathematical operations, such. to a mathematical greatest common divisor.