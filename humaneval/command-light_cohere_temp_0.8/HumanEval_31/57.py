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
This code defines a function is_prime that checks whether a given number n is prime or not. It uses a particular logic to determine primality:

If n is less than or equal to 1, it returns False.

If n is less than or equal to 3, it returns True by default.

It then checks for divisibility by 2 and 3, returning False if either of these numbers divide n.

If n is a square or can be expressed as 6k + 2 or 6k - 1 for some integer k, it returns False.

Finally, it checks if n is a prime number of the form 6k + 1 or 6k - 2 for some integer k, with k greater than 1, and returns True.

This function is self-contained and can pass all the provided tests.