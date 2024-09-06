```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The `greatest_common_divisor` function uses the Euclidean algorithm for computing the GCD. It takes two integers a and b as parameters. If b is 0, it returns a since b cannot be a factor of a nor can a be a factor of b. If b is not 0, the function returns the greatest common divisor of b and a % b, recursively applying the same approach. This algorithm continues until b is 0, at which point the remainder becomes the GCD of the original two numbers.