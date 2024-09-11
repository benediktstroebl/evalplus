### Modp Function in Python
#### Using the Built-in pow() Function for Efficient Computation

We can solve the modp problem efficiently using the built-in `pow()` function in Python, which can compute the power of a number modulo another number in constant time for large numbers.

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The base (2)
        p (int): The modulus

    Returns:
        int: 2^n modulo p

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

Note that we've used the third argument of `pow()` to specify that we want to compute `2^n` modulo `p`. This is more efficient than first computing `2^n` and then taking the modulus.

You can run the function with different inputs to verify its correctness.