```python
def modp(n: int, p: int):
    """
    Calculate 2^n modulo p.

    Args:
    n (int): The exponent.
    p (int): The modulo.

    Returns:
    int: The result of 2^n modulo p.
    """
    result = 1
    base = 2
    while n > 0:
        if n % 2 == 1:
            # If n is odd, multiply the result by base
            result = (result * base) % p
        # Update base and n for the next iteration
        base = (base * base) % p
        n = n // 2
    return result


# Test cases
print(modp(3, 5))       # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))     # Expected output: 1
print(modp(3, 11))      # Expected output: 8
print(modp(100, 101))   # Expected output: 1
```

This script uses a while loop to calculate the result of 2^n modulo p. It starts with a base of 2 and updates it by squaring it and taking modulo p in each iteration. If n is odd, it multiplies the result by the current base and takes modulo p to avoid large numbers. The final result is returned after the loop finishes.