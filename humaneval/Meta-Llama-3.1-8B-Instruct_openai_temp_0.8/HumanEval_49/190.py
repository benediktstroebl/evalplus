```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    Parameters:
    n (int): The exponent.
    p (int): The modulo.

    Returns:
    int: The result of 2^n modulo p.

    Note:
    Be aware of numerics, as this operation can be affected by precision issues.
    """
    # Use the built-in pow function with three arguments to efficiently compute the modulus
    return pow(2, n, p)

# Test cases
if __name__ == "__main__":
    print(modp(3, 5))  # 3
    print(modp(1101, 101))  # 2
    print(modp(0, 101))  # 1
    print(modp(3, 11))  # 8
    print(modp(100, 101))  # 1
```

This script defines a function `modp(n, p)` that uses the `pow` function to efficiently compute `2^n modulo p`. The `pow` function with three arguments (`base`, `exponent`, `modulo`) is used to compute the modulus, which helps to avoid precision issues that can arise when computing large powers modulo a number. The test cases are included in the script to demonstrate the function's correctness.