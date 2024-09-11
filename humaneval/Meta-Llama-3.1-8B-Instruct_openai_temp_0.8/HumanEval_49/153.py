```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.
    
    Be aware that for large inputs, due to the properties of modular arithmetic,
    2^n % p can be efficiently computed without explicitly calculating 2^n.
    
    Parameters:
    n (int): The exponent.
    p (int): The modulus.
    
    Returns:
    int: 2^n modulo p.
    """
    res = 1
    base = 2
    
    # Use repeated squaring to efficiently compute 2^n % p
    while n > 0:
        # If n is odd, multiply the result by base
        if n % 2 == 1:
            res = (res * base) % p
        
        # Square the base and halve n
        base = (base * base) % p
        n //= 2
    
    return res

# Test cases
if __name__ == "__main__":
    print(modp(3, 5))      # 3
    print(modp(1101, 101))  # 2
    print(modp(0, 101))     # 1
    print(modp(3, 11))      # 8
    print(modp(100, 101))   # 1
```

This script defines a function `modp` that efficiently calculates `2^n` modulo `p` using the repeated squaring algorithm, which reduces the time complexity of the calculation to O(log n) compared to the naive approach of calculating `2^n` explicitly and then taking the modulus. The test cases at the end demonstrate the correctness of the function.