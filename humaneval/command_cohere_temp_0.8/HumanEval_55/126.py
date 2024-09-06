```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single argument n, which returns the n-th Fibonacci number. The base case checks if n is less than 2, returning n if so. Otherwise, it recursively calls fib(n-1) and fib(n-2) and returns their sum. This effectively calculates the Fibonacci sequence by recursion, providing an elegant solution to the problem.