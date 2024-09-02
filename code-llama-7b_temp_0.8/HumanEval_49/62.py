

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
    # Compute 2^n modulo p
    # 2^n = 2^(n%logp)
    # 2^n modulo p = 2^(n%logp) modulo p
    # base=2
    # exponent=n
    # modulo=p
    # return pow(base, exponent, modulo)
    # (Algorithm described at: https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/)
    x = 1
    while n > 0:
        if n & 1 == 1:
            x = x * p % 10
        p = p * p % 10
        n >>= 1
    return x

