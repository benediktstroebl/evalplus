Here is a self-contained Python script that defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers `a` and `b`:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    if a == 0:
        return b
    if b == 0:
        return a

    # Use Euclidean Algorithm
    while a != 0:
        q = b // a
        b %= a
        a = q
    while b != 0:
        q = a // b
        a %= b
        b = q

    return a
```
This function performs a brute force approach by attempting to divide until the GCD is found. It uses the maximum number for `a` and `b` and returns their greatest common divisor.