```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```
This recursive algorithm is inspired by the Euclidean algorithm. It returns the greatest common divisor of two integers a and b. If either a or b is zero, it returns the non-zero number. Otherwise, it calls the function recursively with the arguments b%a and a. This approach terminates because the absolute value of the output of b%a decreases with every recursive call. Specifically, the output of b%a is closer to 0 than the output of a. Closer-to-zero numbers are easier to compute GCD for, so this approach converges quickly. It is concise and efficient.