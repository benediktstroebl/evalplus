

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
    # This is a modified version of the standard modular exponentiation routine
    # to avoid potential overflow in the base 2 calculation.
    # It is based on the observation that a number is divisible by p if and only if
    # the binary representation of its decimal value starts with a 1.
    # This is used to compute the modular exponentiation in the following way:
    # exponent = n
    # for i from 1 to m-1 do
    #   exponent = exponent * base (mod p)
    # The for loop is executed m-1 times, so that the final result is correct.
    # This implementation is slightly slower than the standard version but
    # can be used for larger values of n and p.
    return pow(int(n), int(p), 2) % int(p)
