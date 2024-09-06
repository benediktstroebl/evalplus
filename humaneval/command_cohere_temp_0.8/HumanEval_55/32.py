```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python code defines a function fib that calculates the n-th Fibonacci number. The base case checks if n is less than or equal to 1, returning n if so. Otherwise, the function recursively computes the Fibonacci number for n by summing the results of the (n-1)th and (n-2)th Fibonacci numbers, which are themselves the inputs for the (n-3)th and (n-4)th Fibonacci numbers, and so on, following the Fibonacci sequence's intrinsic mathematical definition.