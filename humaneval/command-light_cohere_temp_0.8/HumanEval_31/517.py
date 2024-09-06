Here's a Python function that checks if a given number is prime:
```python
def is_prime(n):
    """Returns True if n is prime, False otherwise."""
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
This function uses a simple trial and error method with some optimizations. It starts by checking numbers up to 3 (since all even numbers and numbers - 2 and - 3 are clearly divisible by 3), and then only tests numbers up to the square of the original number, taking 5 at a time to ensure enough trials for bigger numbers.