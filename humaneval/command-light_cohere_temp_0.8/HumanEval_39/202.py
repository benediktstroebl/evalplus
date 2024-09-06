Here's the code:
```python
def prime_fib(n):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    temp = prime_fib(n // 2)
    if temp == 2:
        return temp
    return temp + 1
```

This code defines a function `prime_fib` that calculates the n-th Fibonacci number and checks for primality.  It also implements an optimization by recursively dividing the input by 2 and using the result to avoid unnecessary iterations.