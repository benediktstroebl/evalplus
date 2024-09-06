```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The code defines a recursive function `fib` that calculates the n-th Fibonacci number. It uses two base cases: when n is 1 or 2, it returns the respective value as these are the first two numbers in the series. For n > 2, it recursively calls itself, summing the results of the previous two calls, each corresponding to the previous two Fibonacci numbers in the series.