### Modular Exponentiation
#### Code
```python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The prime modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Handle the edge cases
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (modp(n // 2, p) ** 2) % p
    else:
        return (2 * modp((n - 1) // 2, p) ** 2) % p


# Test cases
if __name__ == "__main__":
    print(modp(3, 5))  # Output: 3
    print(modp(1101, 101))  # Output: 2
    print(modp(0, 101))  # Output: 1
    print(modp(3, 11))  # Output: 8
    print(modp(100, 101))  # Output: 1
```

#### Explanation
This script uses a recursive approach to calculate the modular exponentiation. The function `modp(n, p)` takes two arguments: `n` (the exponent) and `p` (the prime modulus). 

- If `n` is 0, the function returns 1 because any number to the power of 0 is 1.
- If `n` is even, the function calculates `(modp(n // 2, p) ** 2) % p`, which is equivalent to `2^n` modulo `p`.
- If `n` is odd, the function calculates `(2 * modp((n - 1) // 2, p) ** 2) % p`, which is equivalent to `2^n` modulo `p`.

This approach reduces the number of multiplications required to calculate the modular exponentiation. The `**` operator is used for exponentiation. The `%` operator is used for modulus operation. The `//` operator is used for integer division, which discards the remainder.