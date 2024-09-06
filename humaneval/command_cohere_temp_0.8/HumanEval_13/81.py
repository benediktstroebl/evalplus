```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The `greatest_common_divisor` function uses the Euclidean algorithm for computing the greatest common divisor. It replaces the larger number with the remainder of the division of the larger number by the smaller number until the smaller number becomes zero. At this point, the largest number remaining is the GCD of the original two numbers.