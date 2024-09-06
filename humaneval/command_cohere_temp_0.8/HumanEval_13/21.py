```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This script defines a recursive function `greatest_common_divisor` that returns the greatest common divisor of two integers `a` and `b`. It allows for a single call with two arguments and adheres to the problem statement by handling the `a` equaling zero case. This handles the base case and reduces the problem to a single variable as intended.