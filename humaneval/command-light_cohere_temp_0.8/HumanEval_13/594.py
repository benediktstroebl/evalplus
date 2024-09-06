```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input is required.")
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == b:
        return 1
    else:
        return greatest_common_divisor(b, a%b) + 1
```  This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. It first checks if at least one input is provided and raises a ValueError if that's true. It then continues the another case where it handles cases where either a or b are 0, or if a and b are equal. If a inputs are non-zero, it returns 1. Otherwise, it recursively calls the  `greatest_common_divisor` passing the other parameter, and then adds 1 to obtain the result.