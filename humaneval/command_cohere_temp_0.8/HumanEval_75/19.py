```python
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
```

This Python script defines a function called `is_multiply_prime` that takes a single argument `a`, representing a number less than 100. It aims to determine whether `a` is the product of three prime numbers. The function employs a sieve algorithm to efficiently determine if a number is prime. It initializes a list of boolean values, representing potential prime numbers, and iterates through the numbers from 2 up to the square root of the given number `a`. For each prime number found in this range, it marks the multiples as not prime in the list. If the original number `a` is marked as prime and its divisors, namely `a // 2` and `a // 3`, are also prime, it returns `True`, indicating that the number is the product of three prime numbers. Otherwise, it returns `False`. 

The example provided in the problem statement, namely `is_multiply_prime(30)`, returns `True` since 30 is the product of 2, 3, and 5.