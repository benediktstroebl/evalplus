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
This code defines a function is_prime that checks if a given number n is prime. It uses a certain accepted primality criteria, checking divisibility by 2, 3, and 5, as well as checking divisibility by numbers with only two smaller than sqrt(n).  This function returns True if n is prime and False otherwise.