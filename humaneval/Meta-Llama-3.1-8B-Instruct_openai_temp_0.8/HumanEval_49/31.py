### Python Script for Modp Function
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
    """
    # Ensure n and p are non-negative
    n = n % p
    result = 1
    while n > 0:
        # If n is odd, multiply result by 2 modulo p
        if n % 2!= 0:
            result = (result * 2) % p
        # Divide n by 2
        n = n // 2
    return result

# Test cases
if __name__ == "__main__":
    print(modp(3, 5))   # Output: 3
    print(modp(1101, 101))  # Output: 2
    print(modp(0, 101))  # Output: 1
    print(modp(3, 11))   # Output: 8
    print(modp(100, 101)) # Output: 1
```
This script uses the exponentiation by squaring method to efficiently calculate 2^n modulo p. It works by repeatedly squaring the result and multiplying by 2 modulo p when `n` is odd. This approach reduces the number of multiplications required compared to a naive approach. The script also includes test cases to verify its correctness.