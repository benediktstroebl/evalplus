```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = [i for i in primes if n % i == 0]
    return len(divisors) == 3
```

The function `is_multiply_prime(n)` uses a list of known prime numbers to determine if the given number is the product of three prime numbers. The function returns true if the number has exactly three distinct divisors, which indicates that it is the product of three prime numbers.

Here is a test case that verifies the functionality of the given function:
```python
assert is_multiply_prime(30)
assert not is_multiply_prime(44)
```

This test case checks if the function returns true for a known multiply prime number and false for a number that is not a product of three primes.