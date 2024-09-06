```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a recursive function *fib* that returns the n-th Fibonacci number. It takes a single argument *n* which is the index of the Fibonacci number needed. The function will return the value for *n* = 1 and *n* = 2 directly, and for any other value of *n* it will return the sum of the two previous Fibonacci numbers calculated recursively. This is the classic formula for Fibonacci numbers illustrated in the docstring.