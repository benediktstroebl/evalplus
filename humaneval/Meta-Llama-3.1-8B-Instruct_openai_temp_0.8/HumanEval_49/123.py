## Modular Exponentiation using the Exponentiation Operator
### Solution
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
    # Use the built-in pow function to calculate modular exponentiation
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```
### Explanation
The `pow` function in Python can be used with three arguments to calculate the power of a number while performing modular arithmetic. This is more efficient than manually calculating the power and then taking the modulus, especially for large exponents. 

In the test cases, we pass in the exponent `n` and the modulus `p` to the `modp` function and print the results.