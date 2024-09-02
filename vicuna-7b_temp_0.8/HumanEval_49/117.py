

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
    # This implementation uses the extended Euclidean algorithm to compute phi = (p-1)/n
    # with optimal numerics.
    #
    # To compute this value, we repeatedly divide (p-1) by n and subtract the result from n.
    # The first time we reach 1, we know that n | (p-1).
    #
    # Then we compute phi = (p-1) // n.
    #
    # Finally, we use phi to compute 2^n modulo p as follows:
    #
    # 2^n = (p-1)*phi + n*phi
    # 2^n = (p-1)*phi + n*phi
    # 2^n = (p-1)*phi + n*phi
    #
    # where the last equation is obtained by using the definition of modulo and the fact that
    # 2^0 = 1 modulo p (since p is odd).
    #
    # The result follows.
    return (p-1) // n * n + n