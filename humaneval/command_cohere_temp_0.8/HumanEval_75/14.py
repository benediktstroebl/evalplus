```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    factors = []
    for prime in primes:
        while a % prime == 0:
            factors.append(prime)
            a //= prime
            
    return len(factors) == 3
```

The function `is_multiply_prime` checks if the number `a` is the product of three prime factors and returns a boolean value accordingly. It does so by first assuming that the number is divisible by each prime in a list of known primes, and then checking if the number is divisible by each prime multiple times until the number is fully factored into the prime. 

If the number `a` is fully factored into three primes, the function returns `True`, and if not, the function returns `False`. 

Let's address the example provided in the prompt:
```python
print(is_multiply_prime(30))
```
This will print `True` as the program acknowledges that 30 is the product of 2, 3, and 5. 

This approach assumes that the given number is lesser than 100 and that the list of primes is exhaustive for numbers under 100.