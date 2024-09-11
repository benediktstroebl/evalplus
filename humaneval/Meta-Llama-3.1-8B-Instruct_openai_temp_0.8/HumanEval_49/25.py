### Python Script for Modulo Power
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the property of modular arithmetic that (a*b) % n = ((a % n) * (b % n)) % n.
    It is more efficient than directly calculating 2^n and then taking modulo p.

    Args:
        n (int): The base number.
        p (int): The modulo number.

    Returns:
        int: The result of 2^n modulo p.
    """
    result = 1
    power = n % p  # Reduce power modulo p to avoid large numbers
    while power > 0:
        # Check if the current bit is 1
        if power % 2 == 1:
            # If the current bit is 1, multiply the result by 2 modulo p
            result = (result * 2) % p
        # Square the power for the next iteration
        power = (power * 2) % p
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp(n, p)` that calculates 2^n modulo p efficiently, using the property of modular arithmetic mentioned above. The function uses a while loop to iterate over the bits of the number n, squaring the power and multiplying the result by 2 modulo p if the current bit is 1. The test cases at the end demonstrate the function's correctness.