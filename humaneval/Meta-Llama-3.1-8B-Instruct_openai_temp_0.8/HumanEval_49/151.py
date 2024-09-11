### Modulo Power Function
#### Overview

The following Python script defines a function `modp(n: int, p: int)` to efficiently compute `2^n modulo p` using the property of modular exponentiation.

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    :param n: The exponent.
    :param p: The modulus.
    :return: 2^n modulo p.
    """
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result by the base.
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2.
        base = (base * base) % p
        n = n // 2
    return result

# Example usage
if __name__ == "__main__":
    print(modp(3, 5))  # Expected output: 3
    print(modp(1101, 101))  # Expected output: 2
    print(modp(0, 101))  # Expected output: 1
    print(modp(3, 11))  # Expected output: 8
    print(modp(100, 101))  # Expected output: 1
```

This script uses the property of modular exponentiation to efficiently compute `2^n modulo p`. It starts with the base `2` and iteratively squares it while reducing the exponent `n` by half. If `n` is odd at any point, it multiplies the current result by the base before squaring the base and reducing the exponent. This approach ensures that the result is computed modulo `p` at each step, avoiding large intermediate results and reducing the chance of numerical errors.