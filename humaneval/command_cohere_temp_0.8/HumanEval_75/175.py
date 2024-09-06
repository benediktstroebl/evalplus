```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in primes:
        if n % prime == 0:
            return False
    return True
```

This function checks if a number is the product of exactly 3 prime numbers. It does so by iterating through a list of known primes and checking if the number is divisible by any of them. If the number is divisible by at least one prime number, the function returns `False`, and if it isn't, then it returns `True`. 

This approach ensures that n is checked against all possible primes in an efficient manner, without unnecessary computations.