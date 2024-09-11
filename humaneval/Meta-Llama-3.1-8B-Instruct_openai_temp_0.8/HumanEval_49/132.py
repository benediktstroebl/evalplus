```python
def find_order(p: int) -> int:
    """
    Find the Euler's totient function for a given prime number 'p'.
    """
    # Since 'p' is a prime number, its Euler's totient function is 'p-1'
    return p - 1


def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.
    
    This function calculates 2^n modulo p using Euler's theorem, 
    which states that a^φ(n) ≡ 1 (mod n) if a and n are coprime.
    
    :param n: The exponent
    :param p: The modulus (prime number)
    :return: 2^n modulo p
    """
    # Calculate Euler's totient function for 'p'
    order = find_order(p)
    
    # Reduce the exponent 'n' modulo the order
    n = n % order
    
    # Calculate 2^n modulo p using Python's built-in pow function with three arguments
    return pow(2, n, p)


# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script includes a helper function `find_order` to calculate Euler's totient function for a given prime number `p`, and the `modp` function uses this helper function to reduce the exponent `n` modulo the order before calculating the result. The `pow` function with three arguments is used to efficiently calculate `2^n modulo p`.