Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement and satisfies the provided tests as it determines a number to be prime or not. It first handles the edge case of n being less than 2, then iterates from 2 to the square root of n, checking for divisibility. If none is found, the number is prime, thereby passing the provided tests.