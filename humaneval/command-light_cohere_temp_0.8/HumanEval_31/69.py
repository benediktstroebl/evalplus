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
This code defines a function called `is_prime` that checks whether a given number is prime or not. The function uses an algorithm that iterates up to the square root of the number, and checks for divisibility by consecutive odd numbers. The function returns `True` if the number is prime, and `False` otherwise. The function is self-contained and can solve the problem of determining whether a given number is prime or not.