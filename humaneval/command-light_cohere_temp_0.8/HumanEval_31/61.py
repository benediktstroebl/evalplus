```python
def is_prime(n):
    """
    True if the number is a prime, False otherwise.
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
This function, `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. It uses a for iterating through `i` and checks divisibility of `n` by all numbers `i` such that `i * i <= n`. The function also checks for other common prime factors by checking divisibility with `2` and `3` directly, and then iterates up to `i = 5` while checking for divisibility by numbers of the form `i^2i + 2`.