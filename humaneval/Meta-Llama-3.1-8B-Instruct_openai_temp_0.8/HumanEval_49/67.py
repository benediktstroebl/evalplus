```python
def modp(n: int, p: int):
    """
    Return 2^n modulo p.

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
    """
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result

# Test cases
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This script uses a simple loop to calculate 2^n modulo p. It starts with a result of 1, then in each iteration, it multiplies the current result by 2 and takes the modulus p. This process is repeated n times, resulting in 2^n modulo p. The test cases at the end verify that the function works as expected.