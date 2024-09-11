```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The base number.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result
```

Example use cases:

```python
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```