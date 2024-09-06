```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        a, b = 2, 3
        while a <= n:
            if b <= n and n % a == 0:
                return a
            a += 1
            b += a // 3
        return a
```
The function prime_fib(n) computes the n-th Fibonacci number that is also prime. It uses recursion and trial and error to find the prime.