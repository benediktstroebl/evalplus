```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The base number (2 in this case).
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    # Use the built-in pow function with three arguments, 
    # which efficiently computes the power modulo p
    # This avoids potential overflow issues
    return pow(2, n, p)

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))   # 2
print(modp(0, 101))   # 1
print(modp(3, 11))   # 8
print(modp(100, 101))   # 1
```

Note that the `pow` function in Python has a third argument that allows you to compute `a ^ b % c` in a single operation. This is the most efficient way to compute the result modulo `p`.