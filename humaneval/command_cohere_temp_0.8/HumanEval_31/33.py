```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining whether a given number is prime or not. It initially verifies if the number is greater than 1 and then checks if it can be divided evenly by any number between 2 and the target number itself. If no such divisor is found, it returns `True`, indicating that the number is prime; otherwise, it returns `False`. This approach is efficient due to its incremental exploration of potential divisors, aiding in the prompt detection of non-primality.