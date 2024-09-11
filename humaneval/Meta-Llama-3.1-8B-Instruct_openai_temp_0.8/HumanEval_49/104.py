```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    This function uses the property of modular arithmetic that (a*b) % n == ((a % n) * (b % n)) % n.
    This prevents large numbers from being stored in memory, allowing for efficient calculation of large powers.
    
    Args:
        n (int): The power to which 2 should be raised.
        p (int): The modulo value.

    Returns:
        int: The result of 2^n modulo p.
    """
    result = 1
    base = 2 % p  # Precompute 2 % p to prevent large numbers
    while n > 0:
        # If n is odd, multiply the result by base
        if n % 2 == 1:
            result = (result * base) % p
        # If n is even, square the base
        base = (base * base) % p
        # Divide n by 2 (integer division)
        n = n // 2
    return result


# Test cases
if __name__ == "__main__":
    print(modp(3, 5))  # 3
    print(modp(1101, 101))  # 2
    print(modp(0, 101))  # 1
    print(modp(3, 11))  # 8
    print(modp(100, 101))  # 1
```

This script defines a function `modp(n, p)` that calculates 2^n modulo p using the property of modular arithmetic mentioned above. The test cases at the end demonstrate the function's correctness.