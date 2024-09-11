```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    Args:
    n (int): The exponent
    p (int): The modulus
    
    Returns:
    int: 2^n modulo p
    
    Example:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    def pow_mod(base: int, exponent: int, modulus: int) -> int:
        result = 1
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent // 2
            base = (base * base) % modulus
        return result
    
    return pow_mod(2, n, p)

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))   # 8
print(modp(100, 101))  # 1
```
This script defines a function `modp` that takes two parameters `n` and `p`. It uses a helper function `pow_mod` to calculate `2^n` modulo `p`. The `pow_mod` function uses the exponentiation by squaring method to efficiently calculate the power modulo the given modulus. The test cases at the end of the script demonstrate the function's correctness.