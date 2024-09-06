def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Check if the sqrt of a is an integer
        if int(sqrt(a)) == sqrt(a):
            # Split a into three factors
            factors = list(set(factorize(a)))
            if len(factors) == 3 and factors[0] * factors[1] * factors[2] == a:
                return True
    return False
def factorize(n):
    # List of primes starting from 2
    primes = [2]
    # Iterate through numbers from 2 to n
    for i in range(2, n + 1):
        # Check the condition for primality
        if n % i != 0:
            primes.append(i)
    return primes