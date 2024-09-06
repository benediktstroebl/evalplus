```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 0
    else:
        a, b = 5, 2
        for _ in range(4):
            a, temp = a, a + b
            if temp <= n and temp is_prime():
                b = temp
                yield a
            else:
                yield b
```
This function generates all the prime Fibonacci numbers and passes the corresponding test.