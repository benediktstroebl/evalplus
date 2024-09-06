```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a brute-force approach that checks for divisibility among all numbers from 2 to the square root of the target number. It returns 'True' if the number is prime and 'False' if it is not. This method may not be optimal for large numbers, but it works effectively for most cases.