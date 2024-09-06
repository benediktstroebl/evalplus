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
This function, `is_prime`, efficiently checks whether a given number `n` is prime or not. It uses the basic number theory concepts and a loop to perform the necessary tests. 

The function returns `True` if the number is prime, and `False` otherwise.