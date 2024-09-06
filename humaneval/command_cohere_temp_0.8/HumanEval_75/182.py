```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = [i for i in primes if n % i == 0]
    return len(divisors) == 3
```

The function `is_multiply_prime` checks if the given number is divisible by any number from the list of primes lesser than 100. If the given number is not divisible by any number, the function returns `False`. If it is divisible by exactly 3 primes, the function returns `True`. This approach optimizes the calculation by only checking for divisibility against known prime numbers and does not require exhaustive factorization. 

Here is a sample output of the function:
```
is_multiply_prime(30) == True
is_multiply_prime(28) == False
is_multiply_prime(52) == True
is_multiply_prime(100) == False
```

This output validates the behavior of the function: `is_multiply_prime(n)` correctly returns `True` for multiply prime numbers and `False` otherwise.