def iscube(a):
    # Factorize the integer
    factors = []
    for i in range(2, int(a ** (1/3) + 1)):
        while a % i == 0:
            factors.append(i)
            a //= i
    if a != 1:
        factors.append(a)

    # Check if there are three equal factors
    return len(factors) == 3 and factors.count(factors[0]) == 3