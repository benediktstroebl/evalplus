### Modular Exponentiation
Modular exponentiation is a technique used in number theory to efficiently compute the value of `a^n mod m` without having to compute the full value of `a^n`.

### Python Implementation

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n mod p.
    """
    result = 1
    base = 2

    # Use the built-in pow function with three arguments to perform modular exponentiation
    result = pow(base, n, p)

    return result

# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

In this code, the `modp` function uses the `pow` function with three arguments to perform modular exponentiation efficiently. The `pow` function's third argument is the modulus, which prevents the intermediate results from getting too large and avoids numerical overflows.