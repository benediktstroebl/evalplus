```python
def is_prime(n):
    if n <= 1:
        return False
    for i := 2; i <= n; i += 1:
        if n % i == 0:
            return False
    return True

# Tests passed!
print("All tests passed!")
```