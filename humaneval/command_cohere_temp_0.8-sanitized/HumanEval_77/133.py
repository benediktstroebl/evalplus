def iscube(a):
    # Factorize the integer
    factors = []
    for i in range(2, int(a**.5) + 1):
        while a % i == 0:
            factors.append(i)
            a //= i
    if a > 1:
        factors.append(a)
    
    # Check if there are 3 factors of the same number
    return len(factors) == 3 and factors.count(factors[0]) == 3