```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The base number (2 in this case).
    p (int): The modulo number.

    Returns:
    int: The result of 2^n modulo p.
    """
    result = 1  # Initialize result to 1
    while n > 0:  # Loop until n becomes 0
        if n % 2 == 1:  # If n is odd
            result = (result * 2) % p  # Multiply result by 2 and take modulo p
        n = n // 2  # Divide n by 2
    return result

# Test cases
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This script defines the `modp` function, which calculates the result of 2^n modulo p using the property of modular exponentiation, which reduces the number of multiplications by using binary exponentiation. The script then includes test cases to verify the function's correctness.