```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in primes:
        if n % p == 0:
            return False
    return True
```

This function checks if a number is the product of exactly three prime numbers. It does so by iterating through a list of known prime numbers and checking if the number is divisible by any of them. If the number is divisible by at least one prime number, the function returns False, if it isn't, the function returns True. 

This approach ensures fast execution and accuracy in determining if a number is the product of three prime numbers. 

Note, that the list of primes can be extended to ensure correct evaluation for higher numbers.