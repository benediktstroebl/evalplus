```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python script defines a self-contained function called fib that takes an integer n as input and returns the n-th Fibonacci number. The function first checks if n is less than or equal to 1, returning n directly in such cases. Otherwise, the function recursively computes the Fibonacci number by summing the results of the (n-1)th and (n-2)th Fibonacci numbers, which are themselves computed recursively. This script's fib function elegantly defines the Fibonacci sequence in a mathematically sound and computationally efficient manner.