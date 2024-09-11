## Modulo Power Function
### Description
The following Python script defines a function `modp` that calculates 2 raised to the power of `n` modulo `p`.

### Code
```markdown
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulo.

    Returns:
        int: 2^n modulo p.
    """
    result = 1
    for i in range(n):
        result = (result * 2) % p
    return result

# Example usage
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

### Advice
This implementation uses a simple iterative approach to calculate 2^n modulo p. It initializes the result to 1 and then repeatedly multiplies the result by 2, taking the modulo p after each multiplication. This approach avoids potential integer overflow issues that may arise when directly calculating 2^n modulo p.