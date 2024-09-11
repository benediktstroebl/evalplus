```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.

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
    base = 2 % p  # Avoid large numbers by taking 2 modulo p
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n = n >> 1
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```
This script uses the property of modular arithmetic that `(a*b) % n = ((a % n) * (b % n)) % n`. This property allows us to avoid large numbers by taking `2` modulo `p` instead of computing `2^n` directly. The script also uses bitwise shift (`n = n >> 1`) to reduce the exponent by half in each iteration, which makes the loop run faster.