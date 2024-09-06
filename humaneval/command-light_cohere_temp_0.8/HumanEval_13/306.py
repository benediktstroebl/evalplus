```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")

    if a == 0:
        return b
    elif b == 0:
        return a

    # To optimize further, we could do better here
    # by finding the GCD of smaller input and using that
    # to calculate the result.

    return a _math.gcd(a, b)
```