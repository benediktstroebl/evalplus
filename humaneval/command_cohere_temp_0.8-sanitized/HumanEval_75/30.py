def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Count the unique divisors of the number a
        div = set(int(d) for d in factorize(a) if d > 1)
        # Check if the number is the multiplication of exactly 3 primes
        return len(div) == 3
    else:
        return False
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(int(n))
    return factors