```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a brute-force approach bolstered by a check for divisibility up to the square root of the number. It returns True when the number is prime and False when it is not. This method may not be optimal for larger numbers, but it works effectively for most practical applications.