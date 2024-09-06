Here is a self-contained Python function that solves the problem of checking whether a number is a prime:
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

This function employs an algorithm that checks for divisibility by examining divisibility by 2, 3, and numbers creating perfect squares ending in 6. It iterates up additionally checks if the numbers greater than 3 are also prime, which is where the concept starts to become more complex.