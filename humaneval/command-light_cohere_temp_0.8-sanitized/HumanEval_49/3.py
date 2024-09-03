def modp(n, p): 
    """Return 2^n modulo p."""
    return pow(2, n, p) % p