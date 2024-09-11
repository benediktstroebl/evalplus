```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    For very large values of n or p, consider using the built-in pow function with three arguments.

    Args:
        n (int): The base number.
        p (int): The modulo.

    Returns:
        int: The result of 2^n modulo p.
    """
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))   # 2
print(modp(0, 101))   # 1
print(modp(3, 11))   # 8
print(modp(100, 101))   # 1
```

This script defines a function `modp` that calculates 2^n modulo p using a simple loop. The test cases at the end verify that the function works correctly. 

Please note that this function can be slow for very large values of n due to its iterative approach. If you need to handle large values, consider using the built-in `pow` function with three arguments, which is more efficient: `pow(2, n, p)`.