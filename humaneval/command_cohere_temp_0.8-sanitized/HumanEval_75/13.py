def is_multiply_prime(a):
    # Write a Python program to check if a given number is multiply prime
    # Precondition: Number is lesser than 100
    # Postcondition: If the number is the product of 3 prime numbers, return true, else return false

    import math
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    if a < 2 or math.sqrt(a) != int(math.sqrt(a)):
        return False

    for prime in primes:
        if a % prime == 0:
            return False

    return True