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
This code defines a function 'is_prime' that checks if a given number 'n' is prime or not. It uses some basic primality checks like divisibility by 2 and 3, and then further improves the algorithm by iterating up to the square root of the number while checking for divisibility by consecutive odd numbers. 

This function successfully passes all the tests provided in the initial prompt.