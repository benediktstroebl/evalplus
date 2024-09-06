```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a brute-force approach fortified by a optimized loop range. It rightly returns False for non-prime numbers, while rightfully identifying prime numbers as True.