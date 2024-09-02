
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    if a == 0 or a == 1:
        return False

    primes = [i for i in range(2, int(a**0.5)+1) if a % i == 0]

    while len(primes) > 0:
        prime = primes[0]
        if a % prime == 0:
            a /= prime
            primes = [i for i in primes if i % prime!= 0]
        else:
            primes.pop(0)

    return a == 1
