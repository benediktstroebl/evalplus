```python
def modp(n: int, p: int):
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
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
        if n % 2 == 1:  # if n is odd, multiply the result by base
            result = (result * base) % p
        n = n >> 1  # divide n by 2
        base = (base * base) % p  # update base for the next iteration
    return result

# Test the function
if __name__ == "__main__":
    print(modp(3, 5))  # Output: 3
    print(modp(1101, 101))  # Output: 2
    print(modp(0, 101))  # Output: 1
    print(modp(3, 11))  # Output: 8
    print(modp(100, 101))  # Output: 1
```

This script defines a function `modp` that calculates 2^n modulo p efficiently using a binary exponentiation method. It then tests the function with several examples.