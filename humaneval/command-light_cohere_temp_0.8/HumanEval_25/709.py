```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This function takes an integer n as input and returns a list of prime factors of the given number. It does so by iterating through all numbers starting from 2 up until the square root of the number is reached. The square root is found using the formula n ** sqrt(n) and the while loop is terminated when n is no longer divisible by any number less than the square root of n.

The function also checks if the input n is a prime number. If it is, the number itself is returned as a factor.