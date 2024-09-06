def iscube(a):
    # Factorize the integer
    factors = []
    for i in range(2, int(a ** (1/3) + 1)):
        while a % i == 0:
            factors.append(i)
            a //= i
    if a != 1:
        factors.append(a)
    # Filter out the cube factors
    factors = [i for i in factors if i ** 3 == a]
    return len(factors) == 1