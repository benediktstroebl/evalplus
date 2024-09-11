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
    # Handle edge case where n is 0
    if n == 0:
        return 1
    
    # Initialize the result to 2, which is 2^1
    result = 2
    # For each bit in n, multiply the result by 2 if the bit is 1
    for bit in bin(n)[2:]:
        result = (result * result) % p
        # If the bit is 1, multiply the result by 2
        if bit == '1':
            result = (result * 2) % p
    
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp` that calculates `2^n` modulo `p`. It uses a binary representation of `n` to efficiently calculate the result. The script also includes test cases to verify the correctness of the function.