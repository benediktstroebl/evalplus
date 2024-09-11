```python
def modpow(n: int, p: int, m: int) -> int:
    """
    Compute (n^p) mod m.

    Args:
    n (int): The base number.
    p (int): The exponent.
    m (int): The modulus.

    Returns:
    int: The result of (n^p) mod m.
    """
    # Initialize the result to 1
    result = 1
    
    # Convert n to its modular equivalent
    n = n % m
    
    # Use exponentiation by squaring to find n^p mod m
    while p > 0:
        # If p is odd, multiply the result by n
        if p % 2 == 1:
            result = (result * n) % m
        
        # Square n and divide p by 2
        n = (n * n) % m
        p = p // 2
    
    return result

def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    return modpow(n, p, p)

# Test cases
print(modp(3, 5))   # Expected output: 3
print(modp(1101, 101))   # Expected output: 2
print(modp(0, 101))   # Expected output: 1
print(modp(3, 11))   # Expected output: 8
print(modp(100, 101))   # Expected output: 1
```

This script first defines a helper function `modpow` that calculates `(n^p) mod m` using the exponentiation by squaring method. It then defines the `modp` function, which is a wrapper around `modpow` that calculates `2^n modulo p`. Finally, it includes the test cases from the original problem statement.