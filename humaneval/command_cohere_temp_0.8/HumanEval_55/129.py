```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The code defines a recursive function `fib` that calculates the n-th Fibonacci number. It uses two base cases: when n is 1 or 0, it returns n directly (since the first two numbers in the Fibonacci sequence are 0 and 1). For larger n, it recursively calls itself, adding the results of the two previous recursive calls together, which aligns with the mathematical definition of the Fibonacci sequence.