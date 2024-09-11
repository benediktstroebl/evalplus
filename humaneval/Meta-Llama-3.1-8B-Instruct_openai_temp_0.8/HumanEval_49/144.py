Here's a Python script with a self-contained function to solve the problem:
```markdown
### Modulo Power Function
#### Python Function to Calculate 2^n Modulo p
```python
def modp(n: int, p: int) -> int:
    """
    Calculate 2^n modulo p using the built-in pow function.

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
    """
    # Use the pow function with three arguments to calculate 2^n modulo p efficiently
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```
This script uses the built-in `pow` function in Python, which can take three arguments: the base, the exponent, and the modulus. This allows us to calculate `2^n modulo p` efficiently and accurately. The script also includes test cases to verify its correctness.