```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    The function uses the property of modular arithmetic that (a*b) mod n = ((a mod n) * (b mod n)) mod n
    to avoid large intermediate results.

    Args:
        n: The exponent.
        p: The modulus.

    Returns:
        The result of 2^n modulo p.
    """
    result = 1  # Initialize result to 1
    base = 2  # Base number is 2
    while n > 0:  # Continue the loop until n is 0
        if n % 2 == 1:  # If n is odd
            result = (result * base) % p  # Multiply result with base and take modulus p
        n = n >> 1  # Right shift n by 1, effectively dividing by 2
        base = (base * base) % p  # Square the base and take modulus p
    return result


# Test cases
if __name__ == "__main__":
    print(modp(3, 5))  # Expected output: 3
    print(modp(1101, 101))  # Expected output: 2
    print(modp(0, 101))  # Expected output: 1
    print(modp(3, 11))  # Expected output: 8
    print(modp(100, 101))  # Expected output: 1
```

This script defines a function `modp(n, p)` that calculates `2^n` modulo `p` efficiently using the property of modular arithmetic that `(a*b) mod n = ((a mod n) * (b mod n)) mod n`. It then includes test cases to verify the correctness of the function.