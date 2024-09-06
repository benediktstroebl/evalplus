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
This function, `is_prime`, determines whether a given number is a prime or not. It starts with an if the number is less than or equal to one, returning `False` as it is not prime. It then checks for divisibility by 2 and 3, returning `False` if the number is divisible by either of these two. If the number is not divisible by 2 or 3, the function checks if the number is divisible by any odd number up to the square root of the number, returning `False` if it is divisible by any such number. If none of these divisors are found, the function returns `True`, indicating that the number is prime.