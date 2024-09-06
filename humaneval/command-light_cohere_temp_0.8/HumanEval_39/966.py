```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        prime = 3
        is_prime = True
        for i in range(2, int(n ** 0.5)):
            if is_prime == True and i != n:
                is_prime = False
                break
        return prime
```