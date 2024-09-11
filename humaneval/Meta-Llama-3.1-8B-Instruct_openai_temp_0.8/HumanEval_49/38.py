```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.

    Example:
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
        n //= 2
        base = (base * base) % p
    return result
```
This Python script uses a while loop to calculate the result of 2^n modulo p. Inside the loop, it checks if the exponent `n` is odd. If it is, it calculates the result of the current power of 2 modulo `p`. Then, it divides `n` by 2 and calculates the next power of 2 modulo `p`. This process continues until `n` becomes 0, at which point the function returns the result.

Note that this script uses the property of modular arithmetic that `(a * b) % p = ((a % p) * (b % p)) % p`. This allows us to avoid large intermediate results and calculate the final result modulo `p` at each step.

Also, note that this script assumes that `p` is a prime number. If `p` is not a prime number, the result may not be correct due to the properties of modular arithmetic.