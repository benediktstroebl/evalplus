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

The function uses trial division, primality tests, and checks for divisibility by 2 and 3 to determine if a given number is prime. It handles edge cases, such as 2 and 3, and the condition for square numbers to efficiently reduce the search space.