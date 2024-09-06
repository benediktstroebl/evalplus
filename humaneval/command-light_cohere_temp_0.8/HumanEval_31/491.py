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
This function `is_prime` accepts an integer `n` as input and determines whether it is a prime number. It follows these steps to accomplish this:
- The function returns `False` if `n` is less than or equal to 1.
- If `n` is less than or equal to 3, the function returns `True`.
- If `n` is even or is divisible by 3, the function returns `False`.
- The function starts checking for divisors up to the square root of `n` and checks if `n` is divisible by any of these divisors.
- If the function returns `True` if `n` does not have any divisors.

This code can solve the given problem and pass all the corresponding tests.