

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
    # Use the algorithm "Chinese Remainder Theorem"
    # Find modulo of n % p, p^2, p^3, ..., p^n
    # Find x = gcd(n, p^k)
    # s = n / x
    # Take x^n mod p^k
    # s = n % p^k
    # x = x^k + s * x^(k-1) mod p^(k+1)
    # Repeat until x is correct
    # x = gcd(s, p^k)
    # x = x / (s / gcd(x, p^(k+1)))
    # x = x^k + s * x^(k-1) mod p^(k+1)
    # Repeat until x is correct
    # Repeat this algorithm for all p^k
    # Get the correct x by comparing the result of x^n mod p^n
    d = n % p
    x = pow(p, int(np.log2(d)))
    for k in range(1, len(p)):
        d = x**k + d*x**(k-1) % p**(k+1)
    return d
