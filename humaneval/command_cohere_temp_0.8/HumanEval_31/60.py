```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a brute-force approach fueled by a foundational optimization: testing only up to `n ** 0.5`. This is because a number can be factored by a smaller prime if and only if it is divisible by it. This ensures the function's effectiveness in confirming prime status while maintaining clarity and conciseness.