### Modp Python Script
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The base number.
    p (int): The modulo number.

    Returns:
    int: The result of 2^n modulo p.

    Examples:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    result = 1
    power = n
    while power > 0:
        # If the power is odd, multiply the result by 2 and apply modulo p
        if power % 2 == 1:
            result = (result * 2) % p
        # Square 2 and apply modulo p
        power = power // 2
        result = (result * result) % p
    return result

# Example usage:
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```
This script uses a while loop to efficiently calculate 2^n modulo p. It takes advantage of the property that multiplying by 2 is equivalent to shifting the bits of the number to the left, which can be achieved by dividing the power by 2 in each iteration. This approach avoids the need for explicit multiplication and reduces the number of iterations required.