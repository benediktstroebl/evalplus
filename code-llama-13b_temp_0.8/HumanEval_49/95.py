

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
    assert n >= 0
    assert p > 0

    n, p = int(n), int(p)
    power_of_two = 1
    double_of_power_of_two = 1
    result = 1

    while double_of_power_of_two <= n:
        double_of_power_of_two <<= 1
        power_of_two <<= 1
        power_of_two %= p

        if double_of_power_of_two <= n:
            result *= power_of_two
            result %= p

    return result
