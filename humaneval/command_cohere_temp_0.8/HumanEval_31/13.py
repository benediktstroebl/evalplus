```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function incorporates an optimized approach that checks only the divisibility of a number by integers up to its square root. This is informed by the fact that prime numbers are divisible only by 1 and themselves.

The function returns True if the number is prime, and False otherwise. This aligns with the problem statement's requirement.