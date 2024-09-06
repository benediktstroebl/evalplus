```python
def prime_fib(n: int):
    if n <= 1:
        return n
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i
```

This function generates the n-th prime Fibonacci number by iterating from 2 to n and checking for divisibility by all numbers from 2 to the square root of the current number.