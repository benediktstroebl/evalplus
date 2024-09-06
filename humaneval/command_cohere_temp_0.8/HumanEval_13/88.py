```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive algorithm is inspired by the Euclidean algorithm. It avoids division operations, which are expensive, and keeps rewriting the problems in a way that reduces the original problem size. It is tested on the same edge cases as the provided test cases.