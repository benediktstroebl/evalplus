

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
    # n is odd
    if n % 2 == 0:
        return pow(2, n // 2, p)
    # n is odd, so (2^n) % p = 2^(n-1) % p = 2^(n-2) % p = ... = 2 \* 2^(n-2) % p = 2^(n-2) (mod p)
    # so (2^n) % p = 2^(n-1) % p = 2^(n-2) % p = ... = 2
    # Therefore, 2^n mod p = 2^n % p = (2^(n-1) % p) \* (2^(n-2) % p) \* ... \* (2 % p)
    # Let x = 2^(n-1) % p
    # Then x^2 % p = 2^n % p = (x^2) \* (2^(n-2) % p) \* ... \* (2 % p)
    # Let y = 2^(n-2) % p
    # Then y^2 % p = (y^2) \* (2^(n-3) % p) \* ... \* (2 % p) = (y \* (2^(n-2) % p)) \* (2^(n-3) % p) \* ... \* (2 % p)
    # Repeat this process until you get to the innermost loop, where you have:
    # y^2 % p = (y \* (y^2) % p) \* (2^(n-3) % p) \* ... \* (2 % p)
    # Canceling the outermost term, you get:
    # y^2 % p = (y^2) \* (2^(n-3) % p) \* ... \* (2 % p) = (2^(n-2) % p)^2 % p = (2^(n-2) % p \* 2^(n-3) % p) \* ... \* (2 % p)
    # Repeat this process until you get to the outermost loop, where you have:
    # (
