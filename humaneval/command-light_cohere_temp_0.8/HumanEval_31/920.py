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
This function, `is_prime`, determines whether a given number is prime or not. It employs several basic heur techniques, such as the Sieve of Eratosthenes and divisibility checks, to achieve this. It then returns `True` if the number is prime and `False` otherwise.