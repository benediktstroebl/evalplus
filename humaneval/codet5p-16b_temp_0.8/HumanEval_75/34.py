
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    is_prime = lambda n: n > 1 and all(n % i for i in range(2, n))
    primes = filter(is_prime, range(2, a // 2 + 1))
    prime_list = list(primes)
    return prime_list[0] * prime_list[1] * prime_list[-1] == a
