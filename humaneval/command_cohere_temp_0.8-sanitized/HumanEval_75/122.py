import unittest
def is_multiply_prime(a):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = set(str(a).split(' '))
    return len(divisors) == 3 and all(divisor in prime_numbers for divisor in divisors)