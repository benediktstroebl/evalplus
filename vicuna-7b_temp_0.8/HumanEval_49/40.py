

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
    # Encode the input as a number of 1's in binary
    digits = str(p - 1).rjust(len(str(n)), '0')
    binary = '0' + digits + str(n)
    # Find the exponent of 2 that gives the desired residue
    exponent = 0
    for digit in binary:
        if digit == '1':
            exponent += 1
    # Compute 2^exponent modulo p
    return (2 ** exponent) % p
