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

This code defines a function `is_prime` that checks whether a given number `n` is prime. It does this by checking various divisibility conditions, such as divisibility by 2 and 3, as well as checking divisibility by numbers that are multiples of `i` for some `i` greater than 3 but less than or equal to the given number.