```python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    
    Args:
        n (int): The base number (2 in this case).
        p (int): The modulo number.
    
    Returns:
        int: The result of 2^n modulo p.
    """
    try:
        # Use built-in pow function with three arguments to compute power modulo p
        # This is more efficient than using the ** operator and then the % operator
        result = pow(2, n, p)
        return result
    except OverflowError:
        # If the result is too large to fit in a Python int, raise an error
        raise ValueError("Result is too large to fit in a Python int")

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))   # 8
print(modp(100, 101))  # 1
```

In this script, the `modp` function uses the `pow` function to compute 2^n modulo p efficiently. The `pow` function with three arguments can compute the power modulo p directly, which is faster and more memory-efficient than computing the power first and then taking the modulo. If the result is too large to fit in a Python int, the script raises a `ValueError` exception.