```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function examines whether a given number `n` is divisible by any number from 2 to the square root of `n`. If `n` is divisible by any of these numbers, it returns `False`, implying that `n` is not prime. If `n` is not divisible by any of these numbers, it returns `True`, indicating that `n` is prime. This approach is efficient due to its iterative nature and because it only needs to iterate up to `n`'s square root, not `n` itself.

Here is an example of the function's usage:
```python
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```

This demonstrates the function's ability to solve the problem and pass the given tests.