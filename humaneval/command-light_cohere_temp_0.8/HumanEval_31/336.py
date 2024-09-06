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
This function checks if a number is prime or not, using the modulo rule that divides by 2 and 3 won't make the number divisible. It also uses a specific test by trying divisibility up to the square root of the number, and if the number passes all these tests, then it's a prime number.