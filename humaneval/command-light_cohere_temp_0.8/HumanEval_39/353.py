```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        # Find the smallest prime factor of n
        def is_prime(x):
            for i in range(2, int(x)**0.5):
                if x % i == 0:
                    return False
            return True
        for x in range(3, is_prime(n), 2):
            if n % x == 0:
                return x
        return n
```