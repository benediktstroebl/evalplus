### Modular Exponentiation with Python
```python
def modp(n: int, p: int) -> int:
    """
    Calculate 2^n modulo p.

    Args:
    n (int): base number
    p (int): modulo number

    Returns:
    int: result of 2^n modulo p

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

    # use bitwise operations for exponentiation
    while n > 0:
        # if n is odd, multiply result by base
        if n % 2 == 1:
            result = (result * base) % p
        # n is even, divide n by 2
        n = n // 2
        base = (base * base) % p

    return result

# Example usage
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script uses the property of modular exponentiation that states `(a*b) % n = ((a % n) * (b % n)) % n` to efficiently calculate large powers with modulo operation. The script also utilizes bitwise operations for exponentiation to reduce the time complexity from O(n) for naive exponentiation to O(log n).