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

# Test case 1
print("Test case 1 passed:", end)

# Test case 2
6

# Test case 3
10

# Test case 4
13441

# Test case 5
61

# Test case 6
4

# Test case 7
1
```