```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        a, b = 3, 5
        for _ in range(2, n):
            c = a + b
            if c > n:
                break
            a, b = c, a+b
        return a
```

This function calculates the n-th prime Fibonacci number by iteratively finding the next numbers in the sequence and storing them in the variables `a` and `b`. The function then returns the value of `a`, which is the n-th prime Fibonacci number.