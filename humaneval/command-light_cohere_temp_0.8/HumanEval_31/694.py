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
The function `is_prime` accepts an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. 

To verify the function's correctness, we can test it with various inputs, such as numbers greater than 5, even numbers, odd numbers, etc.

You can use this function to determine whether a given number is prime or not in your markdown code block.