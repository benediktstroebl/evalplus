### Mod Power Function in Python
#### Overview
This script provides a function `modp` that calculates the power of a number modulo another number.

#### Code
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulo base.

    Returns:
        int: 2^n modulo p.

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
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
    return result
```

#### Explanation
This script uses a while loop to repeatedly multiply the result by 2 modulo `p`, as long as the exponent `n` is greater than 0. The `while` loop condition checks whether `n` is even or odd. If `n` is odd, we multiply the result by 2 modulo `p` before decreasing `n` by 1. If `n` is even, we simply divide it by 2. This process continues until `n` becomes 0, at which point the function returns the final result.

#### Advice
Use this function to efficiently calculate powers modulo another number, especially when dealing with large numbers where regular exponentiation could result in overflow.