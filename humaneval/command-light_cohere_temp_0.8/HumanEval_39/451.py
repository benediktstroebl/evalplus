```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3  # To keep the loop short
    is_prime = [True, False, True, 3]
    while n > 2:
        if n % 2 == 0 or n % 3 == 0:
            is_prime[0] = False
        n //= 3
    for i, is_prime_val in enumerate(is_prime):
        if is_prime_val:
            return i + 1
    return n  # Return n if all numbers up to it are composite
```