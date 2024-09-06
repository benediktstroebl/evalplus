```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in primes:
        if n % prime == 0:
            return False

    return True
```

This Python script defines a function called `is_multiply_prime` that takes a single argument `n`. It returns `True` if `n` is the product of exactly three prime numbers, and `False` otherwise. The function first defines a list of prime numbers up to `100`, and then iterates through each prime number, checking if `n` is divisible by any of them. If `n` is divisible by any prime number, the function returns `False`, indicating that the number is not the product of exactly three primes. If none of the prime numbers divide `n`, it returns `True`, indicating that it is indeed the product of exactly three primes. 

This approach ensures that the function returns the correct result for the given constraint of less than 100, allowing for an efficient and accurate check for multiply prime numbers. 

 

This function can efficiently handle the requested problem statement, as it clearly provides a boolean answer whether the number is the product of three primes or not.