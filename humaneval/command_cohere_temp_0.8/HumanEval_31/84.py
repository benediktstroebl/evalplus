Here's a Python script with a self-contained function `is_prime` that follows the problem statement and hopefully passes the tests provided:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function checks if a given number `n` is less than 2, returns `False`. If `n` is greater than or equal to 2, it iterates from 2 to the square root of `n` (inclusive), and for each iteration, it checks if the given number is divisible by the current number on the iteration. If it is, it returns `False`. If the loop completes without a divisor found, it returns `True`. 

This approach uses a optimized strategy called the **Sieve of Eratosthenes** to efficiently determine if a number is prime or not.

This function can be used to verify prime numbers with Markdown-style test code:
```python
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```

This function should accurately solve the problem of checking if a number is prime or not, according to the provided tests. Let me know if I misunderstood the problem or provided incorrect solutions. I'm happy to refine the response to ensure it aligns perfectly with your requirements.