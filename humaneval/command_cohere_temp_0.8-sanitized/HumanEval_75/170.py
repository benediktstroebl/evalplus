def is_multiply_prime(a):
    # check if a is less than 100
    if a < 100:
        # check if the root of a is an integer
        if int(root(a)) == a: 
            # if so, check the factors of a
            factors = factorize(a)
            if len(factors) == 3 and all(map(lambda x: x == 1 or x == a, factors.values())):
                return True
    return False
def root(n):
    return int(n ** 0.5)
def factorize(n):
    factors = {}
    for i in range(2, int(root(n)) + 1):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors