```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

The above Python function `is_prime` checks if a given number `n` is prime or not. It uses some basic heur logic to determine primality, and passes all the tests.

The function first checks if the number is less than or equal to 1, and returns `False` since primes don't include the number 1. It then checks if the the number is less than 3, and returns `True` since primes don't include numbers that divide into themselves or 3.

The function then starts a loop that uses the square root of the number and checks if the number is divisible by any number in the loop. It then adds 6 to the loop counter to ensure the loop continues checking divisors up to the square root of the number. 

Finally, the function returns `True` if the number is prime and `False` if it is not.