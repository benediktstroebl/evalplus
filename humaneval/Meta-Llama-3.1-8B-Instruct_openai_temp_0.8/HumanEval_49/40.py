### Modular Exponentiation Script
```python
def modp(n: int, p: int) -> int:
    """
    Compute 2^n modulo p, using the property that
    (a * b) % n = ((a % n) * (b % n)) % n.

    Args:
        n (int): The base number, 2 in this case.
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
    return pow(2, n, p)

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))   # 8
print(modp(100, 101)) # 1
```
This script defines a function `modp(n, p)` that computes 2^n modulo p using the `pow` function with three arguments. The first argument is the base (2 in this case), the second is the exponent (n), and the third is the modulus (p). The `pow` function uses the property of modular arithmetic that `(a * b) % n = ((a % n) * (b % n)) % n` to efficiently compute the result modulo p.

The script then includes test cases to demonstrate the function's correctness.