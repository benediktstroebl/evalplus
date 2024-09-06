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
The provided Python function, `is_prime`, checks whether a given number is prime or not. It employs a specific logic to determine primality, including checking divisibility by 2 and 3, and then incrementing a loop by 6 to identify other potential divisors.