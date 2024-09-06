def is_multiply_prime(a):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if a < 100 and a > 1:
        divisors = []
        for prime in prime_numbers:
            if a % prime == 0:
                divisors.append(prime)
        if len(divisors) == 3:
            return True
    return False