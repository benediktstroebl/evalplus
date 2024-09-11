### Modulo Power Function
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    result = 1
    base = 2

    # Use exponentiation by squaring for efficient calculation
    while n > 0:
        # If n is odd, multiply result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2

    return result

# Example use cases
if __name__ == "__main__":
    print(modp(3, 5))  # Output: 3
    print(modp(1101, 101))  # Output: 2
    print(modp(0, 101))  # Output: 1
    print(modp(3, 11))  # Output: 8
    print(modp(100, 101))  # Output: 1
```

This script defines a function `modp(n, p)` that calculates 2^n modulo p efficiently using exponentiation by squaring. The `if __name__ == "__main__":` block includes example use cases to demonstrate the function's behavior.