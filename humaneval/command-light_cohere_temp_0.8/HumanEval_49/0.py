```python
def modp(n, p): 
    """Return 2^n modulo p"""
    import sympy

    two = 2
    p1 = p + 1
    m = 10**9 + 7

    # handles negative p
    if p < 0:
        p = -p
        m = -m
        
    # handle zero input
    if n == 0:
        return 1
        
    # perform calculation
    n_pow = n
    while n_pow < 0:
        n_pow += 1
    n_pow %= m
    result = (n_pow % p1) * two
    result = (result + result) // 2 

    return result
``` 
Do you have any other questions about the code or need help with anything specific?