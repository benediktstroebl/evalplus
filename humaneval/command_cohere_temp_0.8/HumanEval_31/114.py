```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function incorporates an optimization of the brute-force approach, limiting the range of divisors to integers up to the square root of the number. This optimization significantly reduces the number of iterations for larger numbers, making the prime checking process more efficient.

The function returns True if the number is prime and False if it's not, following the problem statement's criteria.