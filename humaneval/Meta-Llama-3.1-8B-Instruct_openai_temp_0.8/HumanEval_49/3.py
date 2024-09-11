```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.

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
    if n == 0:
        return 1
    elif n > 0:
        result = modp(n // 2, p)
        if n % 2 == 0:
            return (result * result) % p
        else:
            return ((result * result) % p) * 2 % p
    else:
        raise ValueError("Exponent cannot be negative")

# Test cases
print(modp(3, 5))
print(modp(1101, 101))
print(modp(0, 101))
print(modp(3, 11))
print(modp(100, 101))
```

This script uses the property of modular arithmetic that states `(a*b) % n = ((a % n) * (b % n)) % n` to efficiently calculate `2^n modulo p`. The function uses a divide-and-conquer approach to break down the problem into smaller sub-problems, which allows it to handle large values of `n` efficiently. 

Note that the function first checks if the exponent `n` is 0, in which case it returns 1. It then checks if `n` is negative and raises a `ValueError` in this case, as the function is not designed to handle negative exponents. 

The function uses integer division `//` and the modulo operator `%` to calculate the result. The `else` clause calculates `2 * result` modulo `p` when `n` is odd, and simply calculates `result * result` modulo `p` when `n` is even. 

The test cases are included at the end of the script to demonstrate the function's behavior.