```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function iterates through numbers from 2 up to the square root of the input number `n`, checking whether `n` is divisible by any of these numbers. If it's not divisible by any, it's considered prime. This aligns with the problem statement, providing a deterministic prime-checking method.

This approach has a time complexity of O(sqrt(n)), where `n` is the number being tested, as it checks divisibility only up to the square root. This is an efficient strategy for checking primality because the chance of divisibility reduces dramatically beyond the square root. 

This function's behavior is defined by the given problem statement, where the tests also provide further clarity on expected behavior. For instance, the function duly returns False for non-prime numbers and True for prime ones.