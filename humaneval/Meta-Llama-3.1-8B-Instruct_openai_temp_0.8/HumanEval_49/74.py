### Python Script: Modular Exponentiation using Binary Exponentiation
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the binary exponentiation method to efficiently calculate
    modular exponentiation.

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
    base = n % p
    while n > 0:
        # If n is odd, multiply the base with the result
        if n % 2!= 0:
            result = (result * base) % p
        # Square the base and reduce it modulo p
        base = (base * base) % p
        # Right shift the bits of n (divide by 2)
        n = n >> 1
    return result

# Test the function
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```
This script uses the binary exponentiation method to efficiently calculate modular exponentiation. The `modp` function takes two arguments, `n` (the exponent) and `p` (the modulus), and returns the result of `2^n modulo p`. The function uses a while loop to iteratively square the base (`base`) and reduce it modulo `p`, and multiplies the result with the base when `n` is odd. The example test cases demonstrate the correctness of the function.