import unittest
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = [div for div in primes if n % div == 0]
    return len(divisors) == 3