```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses Python's built-in properties of exponentiation and modulus.
    It leverages the fact that (a * b) % n = ((a % n) * (b % n)) % n.
    Therefore, we can avoid large intermediate results and prevent overflow.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    result = 1
    base = 2 % p
    while n > 0:
        # If n is odd, multiply the result by the current base
        if n % 2 == 1:
            result = (result * base) % p
        # Move to the next bit and right shift n by 1
        n = n >> 1
        # Update the base by squaring it and taking the modulus
        base = (base * base) % p
    return result

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))   # 8
print(modp(100, 101)) # 1
```

This script uses a while loop to calculate 2^n modulo p in an efficient manner. It keeps track of the result and the current base (2 modulo p) and updates them in each iteration. This approach prevents large intermediate results and avoids overflow. The test cases at the end verify the correctness of the function.