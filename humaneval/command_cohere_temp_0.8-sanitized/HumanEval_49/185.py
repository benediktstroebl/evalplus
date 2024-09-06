def modp(n, p):
    if n < 0:
        return pow(2, n, p)
    elif n == 0 and p > 1:
        return 1
    else:
        return 2**n% p