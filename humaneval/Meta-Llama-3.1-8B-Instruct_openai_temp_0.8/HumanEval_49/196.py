```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 should be raised.
        p (int): The modulo value.

    Returns:
        int: The value of 2^n modulo p.
    """
    # Use the built-in pow function with three arguments to efficiently compute the power modulo p
    # This avoids large intermediate results and potential overflow issues
    return pow(2, n, p)


# Test cases
if __name__ == "__main__":
    # Test the function with the provided example inputs
    print(modp(3, 5))   # Expected output: 3
    print(modp(1101, 101))  # Expected output: 2
    print(modp(0, 101))  # Expected output: 1
    print(modp(3, 11))  # Expected output: 8
    print(modp(100, 101))  # Expected output: 1
```

This script defines a function `modp` that efficiently computes 2^n modulo p using the `pow` function with three arguments, avoiding potential overflow issues. The test cases are included at the end of the script to verify the function's correctness.