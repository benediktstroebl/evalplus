```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 is raised.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    return pow(2, n, p)


# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script uses the built-in `pow` function with three arguments in Python, which computes the power with the given modulus. This approach is more efficient than repeatedly calculating the modulus for each intermediate result.

Alternatively, you could implement the power calculation manually:

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 is raised.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result


# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This implementation has a time complexity of O(n), where n is the power. However, it may still cause overflows for large powers. The `pow` function has a time complexity of O(log n), which is more efficient in practice.