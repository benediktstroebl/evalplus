## Efficient Modulo Power Calculation
### Script
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p, handling numerical precision issues.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    result = 1
    base = 2
    while n > 0:
        # If the current bit is 1, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base for the next iteration
        base = (base * base) % p
        # Right shift the exponent to move to the next bit
        n = n // 2
    return result

# Example usage:
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```
This script uses a binary exponentiation algorithm to efficiently calculate 2^n modulo p. The `modp` function takes the exponent `n` and the modulus `p` as input and returns the result of 2^n modulo p. The function uses a while loop to iterate over the bits of the exponent, squaring the base for each iteration and multiplying the result by the base when the current bit is 1. The result is calculated modulo p at each step to prevent numerical precision issues.