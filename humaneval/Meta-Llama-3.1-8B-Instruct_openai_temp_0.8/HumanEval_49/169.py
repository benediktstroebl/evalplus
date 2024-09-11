```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power.
        p (int): The modulo.

    Returns:
        int: 2^n modulo p.

    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    result = 1
    base = 2
    for _ in range(n):
        if result >= p:
            result %= p
        result = (result * base) % p
    return result

# Example usage:
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))   # Output: 2
print(modp(0, 101))   # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))   # Output: 1
```

This script uses a simple iterative approach to calculate 2^n modulo p. It starts with `result` as 1, then repeatedly multiplies `result` by 2 and takes the modulo p until `result` is greater than or equal to p, at which point it takes the modulo p and continues the process until it has multiplied `result` by 2 `n` times.