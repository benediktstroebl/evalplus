### Modular Exponentiation using Python
#### Problem Statement
Implement the modp function that calculates 2^n modulo p.

#### Solution
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
    # Initialize result to 1 (base case: 2^0 = 1)
    result = 1
    
    # Convert 2 to an integer and calculate 2^n % p
    base = 2
    while n > 0:
        # If n is odd, multiply the result by 2 modulo p
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base modulo p and divide n by 2
        base = (base * base) % p
        n = n >> 1
    
    return result

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))   # 2
print(modp(0, 101))    # 1
print(modp(3, 11))    # 8
print(modp(100, 101))  # 1
```

#### Explanation
This Python script defines a function `modp` that calculates 2^n modulo p. It utilizes the property of modular exponentiation that (a*b) % n = ((a % n) * (b % n)) % n to minimize the risk of overflow when dealing with high values of `n`. The function iteratively squares the base and reduces the exponent by half until the exponent becomes 0.