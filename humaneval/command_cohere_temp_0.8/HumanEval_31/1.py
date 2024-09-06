```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a brute-force approach bolstered by a loop that checks all potential divisors from 2 up to the square root of the number. The function returns false if any divisors are found, and true if no divisors are found, effectively gauging whether the given number is prime.