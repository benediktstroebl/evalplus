### Modulo Power Function
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    Parameters:
    n (int): The base number (2 in this case)
    p (int): The modulo number

    Returns:
    int: The result of 2^n modulo p

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
    base = 2
    while n > 0:
        # If n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp(n, p)` that calculates `2^n modulo p`. It uses a while loop to repeatedly square the base (2) and divide the exponent (n) by 2, until n is 0. If n is odd, it multiplies the result by the base before squaring it. This approach avoids overflow and ensures accurate results for large values of n. The test cases are included at the end to verify the function's correctness.