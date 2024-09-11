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
    # Initialize result to 1, as any number to the power of 0 is 1
    result = 1
    
    # 2 to the power of n modulo p can be calculated using properties of modular arithmetic
    # Specifically, we can use the property: (a * b) % n = ((a % n) * (b % n)) % n
    # This allows us to avoid large intermediate results
    while n > 0:
        # If n is odd, multiply the result by 2 modulo p
        if n % 2 == 1:
            result = (result * 2) % p
        
        # Divide n by 2
        n = n // 2
    
    # Return the final result
    return result

if __name__ == "__main__":
    # Test cases
    print(modp(3, 5))   # 3
    print(modp(1101, 101))   # 2
    print(modp(0, 101))   # 1
    print(modp(3, 11))   # 8
    print(modp(100, 101))   # 1
```

This script defines a function `modp` that calculates `2^n` modulo `p` using a loop and properties of modular arithmetic. It then tests this function with the provided test cases. The `//` operator is used for integer division, ensuring that the result of the division is an integer.