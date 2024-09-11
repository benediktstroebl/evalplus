```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulo base.

    Returns:
    int: 2^n modulo p.
    """
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses a simple loop to repeatedly square the current result and take the modulo by `p`, effectively computing `2^n` modulo `p` efficiently for large values of `n`. The time complexity of this solution is O(n), which is much more efficient than directly calculating `2^n` and then taking the modulo.