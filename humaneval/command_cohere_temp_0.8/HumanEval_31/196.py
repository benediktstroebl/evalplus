```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, incorporating edge cases, and returning 'True' for prime numbers and 'False' otherwise. Feel free to experiment with different test cases, and let me know if you need assistance with any additional problems.