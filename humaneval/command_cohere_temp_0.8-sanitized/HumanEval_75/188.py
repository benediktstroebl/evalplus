def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    if a < 100 and a > 0:
        # Write a faster program to check for prime using sieve method
        primes = [True for i in range(101)]
        p = 2
        while p * p <= a:
            if primes[p] == True:
                for i in range(p * p, a + 1, p):
                    primes[i] = False
            p += 1
        if primes[a] and primes[a // 2] and primes[a // 3]:
            return True
    return False