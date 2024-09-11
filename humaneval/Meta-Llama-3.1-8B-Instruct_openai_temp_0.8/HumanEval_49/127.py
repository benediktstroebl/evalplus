### Modular Exponentiation using Binary Exponentiation
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
    # Handle the special case where n is 0
    if n == 0:
        return 1
    
    # Use binary exponentiation to compute 2^n modulo p
    result = 1
    base = 2 % p  # Reduce the base modulo p
    while n > 0:
        # If n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base for the next iteration
        base = (base * base) % p
        # Right shift n to divide it by 2
        n = n // 2
    
    return result

# Example usage
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```
This script uses binary exponentiation to efficiently compute 2^n modulo p. It handles the special case where n is 0 separately and uses a while loop to repeatedly square the base and multiply the result by the base when n is odd. The modulus operation is performed at each step to prevent large intermediate results.