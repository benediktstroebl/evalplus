### Modulus Power Function
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 is raised.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.

    Example:
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
    while n > 0:
        if n % 2 == 1:  # if n is odd
            result = (result * base) % p
        n = n // 2  # divide n by 2
        base = (base * base) % p  # update base to be base squared modulo p
    return result
```
This script uses the property of modular arithmetic that `(a * b) % n = ((a % n) * (b % n)) % n`. It repeatedly squares the base (initially 2) modulo `p` and updates the result whenever `n` is odd. The time complexity is O(log n) because we divide `n` by 2 in each iteration.