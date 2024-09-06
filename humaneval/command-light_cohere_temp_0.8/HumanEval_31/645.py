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

This function uses trial division to determine if a given number n is prime or not. It iterates up smallest odd prime factor, starting from 5, and continues until n is not divisible by any prime factor less than or equal to the square of the current prime. This method is efficient for determining primality.