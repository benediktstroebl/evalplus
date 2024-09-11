### Modulo Power
#### A Python Script to Calculate 2^n Modulo p

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    :param n: The exponent
    :param p: The modulo value
    :return: The result of 2^n modulo p
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
    for _ in range(n % (p - 1)):
        result = (result * 2) % p
    return result
```

This Python script defines a function `modp` that takes an exponent `n` and a modulo value `p` as input. It calculates the result of 2^n modulo p using a loop that multiplies the current result by 2 and takes the modulo value at each iteration. The loop runs `n` times, but we use `n % (p - 1)` to reduce the number of iterations when `n` is greater than `p - 1`. This is because the powers of 2 repeat modulo `p` with a period of `p - 1`.

The function returns the result of the calculation, which is the value of 2^n modulo p. The docstring provides a description of the function, its parameters, and its return value, as well as some example usage.