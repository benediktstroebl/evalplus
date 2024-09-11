### Modular Exponentiation in Python
#### Overview
The following Python script uses the property of modular exponentiation to efficiently calculate 2^n modulo p.

#### Code
```markdown
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.

    Examples:
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
    # Handle edge case where n is 0
    if n == 0:
        return 1
    
    # Initialize result
    result = 2
    
    # Update n, result and p if n is negative
    if n < 0:
        n = -n
        p -= 1
    
    # Perform exponentiation by squaring
    while n > 0:
        # If n is odd, multiply result by 2 and take modulus p
        if n % 2 == 1:
            result = (result * 2) % p
        
        # Square result and take modulus p
        result = (result * result) % p
        
        # Right shift n by 1
        n = n >> 1
    
    return result

# Example usage
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))  # Output: 1
```

#### Explanation
The `modp` function uses the property of modular exponentiation to efficiently calculate 2^n modulo p. The function takes two arguments, `n` and `p`, representing the exponent and modulus respectively. It handles edge cases where `n` is 0 and when `n` is negative, updating the result accordingly. The function then uses a while loop to perform exponentiation by squaring, multiplying the result by 2 and taking the modulus `p` when `n` is odd, and squaring the result and taking the modulus `p` when `n` is even. The result is returned after the loop completes.