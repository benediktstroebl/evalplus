Here's a Python script that uses the built-in `pow` function with three arguments to compute `a^n % p` efficiently:
```markdown
### Computing 2^n Modulo p
#### Problem Statement

Given two integers `n` and `p`, compute `2^n % p`.

#### Solution

```python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    
    Args:
    n (int): The exponent.
    p (int): The modulus.
    
    Returns:
    int: 2^n % p.
    
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

The `pow` function with three arguments `a`, `n`, and `p` computes `(a^n) % p` efficiently. This is because it uses the optimized exponentiation algorithm to avoid large intermediate results.

In this solution, we use `pow(2, n, p)` to compute `2^n % p`. This is a more efficient and numerically stable way to compute the result.

You can run the script and test the `modp` function with the provided examples to see that it produces the correct results.