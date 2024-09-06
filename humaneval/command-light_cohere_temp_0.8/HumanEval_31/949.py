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
The function `is_prime()` takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function uses various criteria to determine if a number is prime, such as if the number is less than 2 or 3, or if the number is a multiple of 2 or 3, it returns False. If none of these specified conditions are met, the function returns True, indicating that the number is prime.