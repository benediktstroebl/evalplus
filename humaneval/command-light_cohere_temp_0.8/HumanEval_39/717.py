```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    else:
        # Find a prime factor and add one to it
        i = 5
        while i * i <= n:
            if n % i == 0:
                n //= i
                i += 1
            else:
                break
        return n + i + 2
```