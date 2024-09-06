```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The code defines a Python function called `fib` that calculates the n-th Fibonacci number. The base case checks if `n` is less than or equal to 1, returning `n` if so. Otherwise, the function recursively computes the sum of the (n-1)-th and (n-2)-th Fibonacci numbers, leveraging the definition of Fibonacci sequence. This recursive approach efficiently calculates Fibonacci numbers. The function's docstring includes informative usage examples that demonstrate its behavior for various input values.