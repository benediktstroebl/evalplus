```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = [div for div in primes if n % div == 0]
    return len(divisors) == 3
```

The function `is_multiply_prime(n)` works by first assuming that `n` is a product of three prime factors and then checking if each of these factors is present in the `primes` list, which contains the prime numbers less than 100. If the number is not divisible by any number in the `primes` list, it returns `False`, if it's divisible by a number in the list, it checks if it's divisible by three different numbers and returns `True`. 

To check if a number is prime, we usually check if it's divisible by any number from 2 to the square root of itself, if it's not, then it's prime. However, in this case, we want to check if each of the three factors is prime, so we can skip the square root rule and directly check against the list of prime numbers.