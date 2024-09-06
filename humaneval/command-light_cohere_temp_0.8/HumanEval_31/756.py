Here's a self-contained Python function that determines whether a number is prime or not, and it passes the tests you provided:
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
This function checks a number 'n' for primality. It uses a relevant divisibility rules and a loop to perform the necessary tests. The function will return True if the number is prime, and False otherwise. The tests are based on the definition of primality, where a number is prime if it has no divisors less than or equal to its square root.