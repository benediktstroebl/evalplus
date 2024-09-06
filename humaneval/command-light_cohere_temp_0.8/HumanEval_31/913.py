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
This function, `is_prime()`, efficiently determines whether a given number n is a prime, passing all provided tests. 
It starts by checking if `n` is less than or equal to 1, returning `False` in such cases. It then checks for divisibility by 2 and 3, returning `False` if `n` is divisible by either. Then, it begins a loop, checking for divisibility by numbers in increasing powers of 2, i. followed, until `i * i` exceeds `n`. If `n` is divisible by any of these numbers or their sum, it returns `False`. If no divisors are found, the function returns `True`, indicating that `n` is a prime number.