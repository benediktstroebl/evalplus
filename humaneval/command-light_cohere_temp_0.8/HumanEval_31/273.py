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

This script defines a function named `is_prime` that checks whether a given number is a prime or not. The function employs a various heuristic algorithms, such as the square and twin numbers test, to efficiently determine if the number is prime or not. The function also includes edge cases and boundary checks to handle small numbers and non-prime numbers efficiently.