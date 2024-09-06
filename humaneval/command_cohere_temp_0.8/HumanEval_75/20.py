```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = [val for val in primes if n % val == 0]
    return len(divisors) == 3
```

The function `is_multiply_prime` checks if the given number is divisible by each prime in the list up to the square root of the number.  The number is divisible by 3 primes if it is divisible by each prime less than its square root. The list primes contains all prime numbers up to the square root of 100.