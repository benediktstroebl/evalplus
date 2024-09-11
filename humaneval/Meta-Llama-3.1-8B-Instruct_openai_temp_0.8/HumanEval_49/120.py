```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent to which 2 is raised.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    # Use the built-in pow function with three arguments to calculate the power modulo p
    # This is more efficient and accurate than calculating the power first and then taking the modulus
    return pow(2, n, p)


# Test the function
if __name__ == "__main__":
    test_cases = [
        (3, 5),
        (1101, 101),
        (0, 101),
        (3, 11),
        (100, 101),
    ]

    for n, p in test_cases:
        result = modp(n, p)
        print(f"2^{n} mod {p} = {result}")
```

This script defines a function `modp` that calculates `2^n` modulo `p` using the `pow` function with three arguments. The `pow` function is more efficient and accurate than calculating the power first and then taking the modulus, especially for large values of `n`.

The script then tests the `modp` function with the provided test cases.