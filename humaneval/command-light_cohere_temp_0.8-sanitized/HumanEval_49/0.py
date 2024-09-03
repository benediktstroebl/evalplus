def modp(n, p): 
    m = 2 ** n % p
    return m if m!=0 else 1