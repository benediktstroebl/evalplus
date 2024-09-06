```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Input values are invalid: both numbers must be greater than zero")

    if a == 0 or b == 0:
        return 0

    m = min(a, b)
    if m == 0:
        return 0

    # Compute all divisors of m
    divisors = [d for d in range(1, m // 2 + 1) if m % d == 0]

    # Find the greatest divisor among these
    gcd = max(divisors, key=lambda x: x)

    return gcd
```