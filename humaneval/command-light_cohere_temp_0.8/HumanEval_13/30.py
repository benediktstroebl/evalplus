```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    # Sort numbers
    a, b = map(int, (b, a))
    a, b = b, a

    # Remove divisors of smaller number
    while a % b == 0:
        a, b = b, a + b

    # Repeat until b is 0
    while b:
        a, b = b, a % b

    return a
```