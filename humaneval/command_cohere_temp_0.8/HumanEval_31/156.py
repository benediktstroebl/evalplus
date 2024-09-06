Here's a Python script with a self-contained function that solves the prime-checking problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function checks if a given number `n` is prime or not. It first checks if `n` is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of `n` (inclusive), checking whether `n` is divisible by any integer in that range. If `n` is divisible by any of these integers, it returns `False`. However, if `n` isn't divisible by any integer in the range, it returns `True`, indicating that the number is prime.  This algorithm, known as the `Sieve of Eratosthenes`, is efficient and provides an accurate prime-checking mechanism. 
Here is an example of how to use the function:
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
This shows that the function handles all cases correctly according to the given tests.  Another way to understand this function is that it returns True if a number is greater than 1 and there exists no number between 2 and the square root of the number that can evenly divide the number.