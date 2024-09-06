```python
def is_prime(n):
    """
    Check whether a given number is prime.
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
This code defines a function called `is_prime` that checks whether a given number `n` is prime or not. It first handles some edge cases: `n <= 1` returns `False`, `n <= 3` returns `True`. Then, it checks for divisibility by 2 and 3 (which are clearly prime) and returns `False` accordingly. Next, it starts an iterative process using the square root of the number to the power of the number of square roots less than or equal to `n`. The number is tested for divisibility, and if it fails, it returns `False`. The `i` loop continues until the square root of `i` is less than `n`, and if `n` is divisible by `i` or `i + 2`, it returns `False` as well.  Finally, if none of these conditions are satisfied, it returns `True`, indicating that the number is prime.