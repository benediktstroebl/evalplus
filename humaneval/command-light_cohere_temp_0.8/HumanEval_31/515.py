Here is a self-contained Python function that checks whether a given number is a prime or not:
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
This function uses a set of quick checks to determine whether a number is prime or not. It starts by checking numbers less than or equal to 2, then uses a trial-and-error method with consecutive squares to test if the number is divisible by any smaller square up to the square root of the number.