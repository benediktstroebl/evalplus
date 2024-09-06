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
This function checks for primality in a number n, using the `if` statement to check for divisibility by 2, 3, and consecutive odd numbers. The function then returns `True` if the number is prime, and `False` otherwise.