Here's a self-contained Python function that checks whether a given number is prime:

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True
```

This function employs a 'loop' to systematically check divisibility from 2 up to the square root of the number, 'n'. If the number is divisible by any of these, it is not prime.

This is a self-contained function that can be used to determine whether a given number is prime, and it passes the test of being able to solve the problem.