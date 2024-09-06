Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
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
This code defines a function named `is_prime` that checks whether a given number `n` is prime or not. It employs various heur approach, including checking divisibility by 2 and 3, as well as confirming if `n` is a sqrt(i) power with i. The function returns `True` if the input number is prime, and `False` otherwise.