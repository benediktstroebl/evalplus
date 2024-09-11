```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulo.

    Returns:
    int: The result of 2^n modulo p.
    """
    result = 1  # Initialize result to 1
    base = 2  # The base is 2
    while n > 0:
        # If n is odd, multiply the result by the base (2)
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base (2) and divide n by 2
        base = (base * base) % p
        n = n // 2  # Use integer division to avoid float result
    return result


# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the property of modular arithmetic that `(a*b) mod n = ((a mod n) * (b mod n)) mod n`. It repeatedly squares the base (2) and reduces it modulo p, reducing the exponent by half each time, until the exponent is 0. The result is the final value of the result.