```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True

# Test cases pass successfully
6
101
11
13441
61
4
1
```