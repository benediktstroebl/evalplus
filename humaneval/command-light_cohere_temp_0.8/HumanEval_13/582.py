```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input is required")
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    if a <= 0 or b <= 0:
        raise ValueError("Both inputs must be positive")

    # Calculate the GCD using the Euclidean algorithm
    gcd = a + b - (a % b)
    while gcd > 1:
        b = gcd
        gcd = a % b

    return gcd
```
Do you have anything else I can assist you with?