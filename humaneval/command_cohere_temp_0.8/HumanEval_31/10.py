```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function evaluates whether a given number `n` is prime. It first checks if `n` is less than 2, returning `False` if so. Then, it iterates from 2 up to `n - 1` and checks if the given number can be divided evenly by any. If it can, it returns `False`. If it cannot, it returns `True`. 

This algorithm is relatively efficient because it stops the loop when checking if `n` is divisible by `i` and explicitly stops as soon as a divisor is found. Some other efficient approaches include the `divisor-sweep` algorithm and the `Sieve of Eratosthenes`.