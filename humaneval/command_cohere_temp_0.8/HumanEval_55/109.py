```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The code defines a Python function called `fib` that calculates the n-th Fibonacci number. The base case checks if n is less than or equal to 1, returning n if so. Otherwise, the function recursively computes the sum of the (n-1)th and (n-2)th Fibonacci numbers, utilizing the underlying mathematical relationship that defines the Fibonacci sequence.