```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        # base case
        if n % 2 == 0:
            return prime_fib(n-1)
        # check for other prime factors
        i = 3
        while i * i <= n:
            if n % i == 0:
                while n % (i+2) == 0:
                    n = n // (i+2)
                i += 2
            else:
                break
        return i
```