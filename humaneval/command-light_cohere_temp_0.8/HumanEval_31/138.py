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
```
This code defines a function called `is_prime` that checks whether a given number `n` is a prime or not. It uses a
 `Two Number Theorem` which states that a prime number can be of the form 6k ± 1, 6k⁵d ± 1, or k^2 for some integer k. 

This function uses an optimized algorithm and passes all given tests.