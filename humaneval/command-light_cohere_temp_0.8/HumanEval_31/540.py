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
This code defines a function `is_prime` that checks whether a given number is prime or not. The function employs basic primality tests, such as oddity, divisibility rules, and square and double numbers up to n, to determine if the number is prime or not.