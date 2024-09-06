Here is a self-contained Python function that checks whether a given number is a prime, and passes the corresponding tests:
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
This function uses a combination of small prime numbers and Euclidean algorithms to efficiently determine if a given number is prime.

The function returns True if the number is prime, and False otherwise. It also passes all test cases provided in the initial script.