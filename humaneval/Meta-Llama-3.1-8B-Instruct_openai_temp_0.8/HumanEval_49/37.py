### Modulo Power Calculation
#### Description
This script defines a function `modp` that calculates `2^n` modulo `p`.

#### Code
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulo.

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
    for _ in range(n):
        result = (result * 2) % p
    return result
```

#### Explanation
The `modp` function uses a simple iterative approach to calculate `2^n` modulo `p`. It initializes a result variable to 1 and then iterates `n` times, each time multiplying the result by 2 and taking the modulo `p`. This approach avoids potential precision issues that could arise from calculating `2^n` exactly before taking the modulo.