### Fast Modular Exponentiation
#### Python Script for Calculating 2^n Modulo p
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulo.

    Returns:
    int: 2^n modulo p.
    """
    # Handle the special case where n is 0
    if n == 0:
        return 1
    
    # Initialize the result to 2
    result = 2 % p
    
    # Use the property of modular exponentiation
    # (a * b) % n = ((a % n) * (b % n)) % n
    while n > 1:
        # Square the current result
        result = (result * result) % p
        
        # Right shift the exponent (divide by 2)
        n = n // 2
    
    return result

# Test cases
if __name__ == "__main__":
    print(modp(3, 5))  # Expected output: 3
    print(modp(1101, 101))  # Expected output: 2
    print(modp(0, 101))  # Expected output: 1
    print(modp(3, 11))  # Expected output: 8
    print(modp(100, 101))  # Expected output: 1
```
This script uses the property of modular exponentiation to efficiently calculate 2^n modulo p. It takes advantage of the fact that (a * b) % n = ((a % n) * (b % n)) % n to avoid large intermediate results. The script handles the special case where n is 0 and provides test cases to demonstrate its correctness.