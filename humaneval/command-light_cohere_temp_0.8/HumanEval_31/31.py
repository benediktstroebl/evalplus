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
This function `is_prime` takes an integer `n` as an argument and returns `True` if `n` is a prime number, and `False` otherwise. 

This function uses a simple algorithm to determine if a number is prime. It first checks if `n` is less than or equal to 1, in which case it returns `False` as the number is not prime. 

It then checks for specific divisibility relationships: `n` is divisible by 2 or 3, which returns `False`. Then, it uses a square-root calculation to check for divisibility by smaller square numbers, and finally, it returns `True` if none of these conditions are met. 

This function is self-contained and can be used to determine whether a given number is prime or not.