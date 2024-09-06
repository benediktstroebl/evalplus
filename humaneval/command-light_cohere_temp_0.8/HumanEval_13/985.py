Here's the solution:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return greatest_common_divisor(b, a % b)
```
This Python code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers `a` and `b`. The function uses a conditional chain to handle cases: if `b` is 0 or `a` is 0, it returns `b` as the greatest common divisor. If both numbers are non-zero, it recursively calls the function with the divisor `b` and the remainder `a % b`, to find the greatest common divisor.