

def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
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
    power_of_two = 1
    while power_of_two < n:
        power_of_two *= 2
    x = 1
    while power_of_two > 1:
        if n & 1 == 1:
            x = (x * power_of_two) % p
        power_of_two //= 2
        n //= 2
    return x

