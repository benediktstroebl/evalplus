## Python Script to Calculate 2^n modulo p

The following Python script defines a function `modp` that calculates 2^n modulo p.

```markdown
### Python Function to Calculate 2^n modulo p

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    This function uses the property of modular arithmetic that (a*b) % n = ((a % n) * (b % n)) % n.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    return pow(2, n, p)

# Example usage
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script uses the built-in `pow` function in Python, which has a third argument to specify the modulus. This makes the code concise and efficient, while also handling potential numerical overflow issues.
```