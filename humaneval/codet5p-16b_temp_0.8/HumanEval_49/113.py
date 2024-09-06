

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

    assert n >= 0 and n < p, "Invalid arguments"
    power_of_two = 2
    result = 1
    while power_of_two <= n:
        power_of_two *= 2
    while power_of_two > 0:
        if power_of_two & n:
            result = (result * 2) % p
        else:
            result = (result * 2) % p
        power_of_two //= 2
    return result

