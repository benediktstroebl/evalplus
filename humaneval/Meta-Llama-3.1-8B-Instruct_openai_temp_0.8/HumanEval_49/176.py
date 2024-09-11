### Python Implementation of Modular Exponentiation
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Handle edge case where p is 1
    if p == 1:
        return 0
    
    result = 1
    # Use binary exponentiation to efficiently compute the power
    while n > 0:
        # If the current bit is 1, multiply the result by 2^k (mod p)
        if n % 2 == 1:
            result = (result * 2) % p
        # Divide the exponent by 2 (right shift) for the next iteration
        n = n // 2
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```
This script uses the binary exponentiation method to efficiently compute the power of 2 modulo p, which is a common technique in number theory and cryptography. The `while` loop iterates over each bit of the exponent, and if the bit is 1, it multiplies the result by 2^k (mod p). This reduces the number of multiplications required compared to a naive approach.