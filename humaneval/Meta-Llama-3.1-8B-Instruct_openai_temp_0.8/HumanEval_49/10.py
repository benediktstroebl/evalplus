### Modulo Power Function
A Python function that calculates the modulus of a number raised to a power.

#### Code
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 is raised.
        p (int): The modulus.

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
    return pow(2, n, p)
```

#### Explanation
The `pow` function in Python returns the first argument raised to the power of the second argument modulo the third argument. In this case, we're raising 2 to the power of `n` modulo `p`. This approach is more efficient than using a loop to calculate the power and then taking the modulus, as it avoids the need to store large intermediate values.