```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The base number.
    p (int): The modulus number.

    Returns:
    int: The result of 2^n modulo p.
    """
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply result with base
        if n % 2 == 1:
            result = (result * base) % p
        # n is even, divide n by 2
        n = n // 2
        # Update base to its square modulo p
        base = (base * base) % p
    return result


# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script defines a function `modp(n, p)` that efficiently calculates 2^n modulo p using a binary exponentiation approach. The function initializes a result variable to 1, a base variable to 2, and then iteratively updates the result and base according to the binary representation of n. The test cases at the end demonstrate the function's correctness.