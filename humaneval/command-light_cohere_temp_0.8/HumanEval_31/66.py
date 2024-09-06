Here's the solution to the Markdown code block provided earlier:

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

This function `is_prime` takes an integer `n` as input and checks if it's prime or not. It performs a simple and efficient checks until it reaches the square root of the number, or until the number is even or contains only prime factors.