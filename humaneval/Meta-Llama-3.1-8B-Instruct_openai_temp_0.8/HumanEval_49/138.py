### Modular Exponentiation with Python
#### Using the Built-in `pow` Function

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Use the built-in pow function with three arguments for modular exponentiation
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

### Modular Exponentiation with Manual Implementation

If you want to implement it manually without using the `pow` function, you can use the following script:

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Handle special cases
    if p == 1:
        return 0
    result = 1
    base = 2 % p  # Precompute base modulo p
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        n //= 2
        base = (base * base) % p
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```