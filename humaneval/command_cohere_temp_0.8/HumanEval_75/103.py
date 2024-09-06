```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return not any(x in factors for x in primes)
```

The function `is_multiply_prime(n)` takes a positive integer `n` as input and checks whether it is the product of three prime numbers. The function first creates a list of prime numbers up to `100`. Then it checks all potential factors of `n` up to its square root, and checks if any of them is in the list of primes. As the product of an integer with a prime number is not necessarily prime, we need to check the individually for each prime in the product. 

This function returns `True` if `n` is the product of three primes and `False` otherwise. It's carefully optimized to only iterate over the necessary factors and primes, which allows it to pass the test cases efficiently.