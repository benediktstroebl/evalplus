```python
def modp(n: int, p: int):
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 is raised.
        p (int): The modulo value.

    Returns:
        int: The result of 2^n modulo p.

    Examples:
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
    two = 2
    while n > 0:
        if n % 2 == 1:
            result = (result * two) % p
        n = n // 2
        two = (two * two) % p
    return result
```

This script uses the property of modular arithmetic that `(a*b) % n = ((a % n) * (b % n)) % n` to avoid large numbers. It also uses the property of exponentiation that `2^(n/2) = (2^2)^(n/4)`, which reduces the number of multiplications required. The time complexity of this script is O(log(n)).