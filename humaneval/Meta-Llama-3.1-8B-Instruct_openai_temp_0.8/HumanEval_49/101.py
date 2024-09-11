Here's a Python script that solves the problem:
```markdown
### Modulus Power Function

This script calculates the modulus power function (modp) which returns 2^n modulo p.

#### Code

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.

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
    base = 2
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n = n // 2
    return result
```

#### Usage

To use this function, simply call it with the desired exponent and modulus as arguments.

```python
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script uses a while loop to efficiently calculate the modulus power function by reducing the base and exponent modulo p at each iteration. This is necessary to avoid large intermediate results that could exceed the maximum limit of an integer.
```