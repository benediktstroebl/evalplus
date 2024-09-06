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
This code defines a function named `is_prime` that checks whether a given number `n` is prime or not. The function uses a `if` statement to handle small numbers and returns `True` for prime numbers and `False` otherwise. The function also uses factors to divide by 2 and 3 and then checks divisibility by smaller numbers up to the square root of the input number. The `while` loop is used to check divisibility by numbers of the form `i^2 + 2i` up to the square root of `n`. 

This self-contained function solves the problem of identifying prime numbers and passes the tests provided.