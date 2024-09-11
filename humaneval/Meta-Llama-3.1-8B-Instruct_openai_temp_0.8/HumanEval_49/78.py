```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    :param n: The base number
    :param p: The modulus
    :return: The result of 2^n modulo p
    """
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result

# Test cases
if __name__ == "__main__":
    test_cases = [
        (3, 5),
        (1101, 101),
        (0, 101),
        (3, 11),
        (100, 101),
    ]
    for n, p in test_cases:
        print(f"modp({n}, {p}) = {modp(n, p)}")
```

This script defines the `modp` function, which calculates 2^n modulo p using a simple iterative approach. The function returns the result of the modulo operation. The script also includes a test case section to verify the function's correctness with the provided examples.