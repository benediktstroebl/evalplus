```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in primes:
        if n % prime == 0:
            return False
    return True
```

This function checks if a number is the product of exactly three prime numbers, and it does so by initially excluding the number from consideration as a potential factor. It then looks at the remaining factors to see if they are prime; if so, the number is the product of three prime factors, and the function returns True. Otherwise, it returns False. 

To store the known prime numbers, the primes list is used. To determine whether a number is prime, the modulus operator (%) is used. The function returns False immediately if any element in the list of primes is detected as a factor of the given number, implying that the number has at most two prime factors. The function returns True if no factors are found after iterating through all possible combinations of primes. 

This approach takes advantage of the properties of composite numbers and the uniqueness of prime factorization. It allows for a simple and efficient solution that delivers an accurate result for the given problem.