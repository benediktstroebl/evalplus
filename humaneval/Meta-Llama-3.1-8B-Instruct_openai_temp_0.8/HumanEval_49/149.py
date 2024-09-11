### Modular Power Function
```python
def modp(n: int, p: int) -> int:
    """
    Returns 2^n modulo p (be aware of numerics).

    Args:
        n (int): Exponent.
        p (int): Modulus.

    Returns:
        int: 2^n modulo p.
    """
    # Use built-in pow function with three arguments to compute modular exponentiation
    return pow(2, n, p)


# Example use cases
if __name__ == "__main__":
    print(modp(3, 5))     # Output: 3
    print(modp(1101, 101))    # Output: 2
    print(modp(0, 101))     # Output: 1
    print(modp(3, 11))     # Output: 8
    print(modp(100, 101))   # Output: 1
```
This script uses the `pow` function with three arguments to efficiently compute the modular exponentiation. The third argument specifies the modulus. This approach is more efficient and numerically stable than using a loop to repeatedly calculate the modulus.