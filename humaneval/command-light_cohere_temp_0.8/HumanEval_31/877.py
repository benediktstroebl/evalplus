Here's the solution for the markdown code block:
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

The function `is_prime` takes an integer `n` as input and checks whether it is prime or not. It first handles some edge cases and then employs a trial-and-error strategy to determine if the number is prime or not.