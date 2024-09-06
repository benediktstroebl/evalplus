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
This function is designed to determine if a given number n is a prime or not. It uses a the simple logic to check for prime numbers: numbers less than 2 and less than 3 are prime, numbers divisible by 2 or 3 are not prime, and finally, it checks for divisibility up to the square root of i, incrementing by 6 until the number exceeds the square root of i. This function effectively determines if the watched against the above conditions.