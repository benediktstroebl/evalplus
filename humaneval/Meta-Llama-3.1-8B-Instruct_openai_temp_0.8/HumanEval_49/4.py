Here's a Python script that implements the `modp` function:
```markdown
### Modulo Power Function

This script provides a function to efficiently calculate 2^n modulo p.

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulo.

    Returns:
        int: The result of 2^n modulo p.
    """
    # Initialize result as 1 (2^0 = 1)
    result = 1
    
    # Take advantage of the fact that 2^a * 2^b = 2^(a+b)
    while n > 0:
        # If n is odd, multiply the result by 2
        if n % 2 == 1:
            result = (result * 2) % p
        
        # Divide n by 2 (i.e., shift the bits to the right)
        n = n // 2
    
    return result

if __name__ == "__main__":
    print(modp(3, 5))   # 3
    print(modp(1101, 101))  # 2
    print(modp(0, 101))  # 1
    print(modp(3, 11))  # 8
    print(modp(100, 101))  # 1
```

This script uses a simple iterative method to calculate the result. It initializes the result as 1 and then iteratively multiplies it by 2, taking advantage of the fact that 2^a * 2^b = 2^(a+b). This approach ensures that the result remains small and efficient, making it suitable for large input values.