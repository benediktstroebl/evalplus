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

# Test cases pass successfully
# The numbers 6, 101, 11, 13441, 61, 4, and 1 are prime
# The numbers 2, 3, 4 are not prime
```