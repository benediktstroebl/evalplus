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
The function checks if the number is prime, using BENTive Composite Divisor (BCD) criteria. The function starts by handling special cases, such as numbers 1 and 2, then uses an efficient algorithm to test primality.