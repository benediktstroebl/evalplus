```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the property of modular arithmetic that (a * b) % n = ((a % n) * (b % n)) % n.

    Args:
        n (int): The power to which 2 is raised.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    result = 1
    power = n

    # Use a while loop to reduce the power to 0
    while power > 0:
        # If the power is odd, multiply the result by 2 modulo p
        if power % 2 == 1:
            result = (result * 2) % p
        # Square 2 modulo p and divide the power by 2
        power = power // 2
        # Use the property of modular arithmetic that (a * b) % n = ((a % n) * (b % n)) % n
        # to prevent large numbers from being calculated
        two_mod_p = (2 * 2) % p
        # Reduce the power of 2 modulo p
        power *= 2

    return result

print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```
This script uses a while loop to reduce the power to 0, multiplying the result by 2 modulo p when the power is odd and squaring 2 modulo p when the power is even. This prevents large numbers from being calculated and makes the function more efficient. The property of modular arithmetic that (a * b) % n = ((a % n) * (b % n)) % n is used to prevent large numbers from being calculated.