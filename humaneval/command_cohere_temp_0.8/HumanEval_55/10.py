```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python code defines a function fib that calculates the n-th Fibonacci number. The base cases (n=1 and n=2) are handled first, returning n and 1 respectively. For larger n, the function recursively computes the sum of the previous two Fibonacci numbers, effectively reaching the desired sequence. This approach, while conceptually simple, can become computationally inefficient for larger values of n due to redundant recursive calculations. However, it demonstrates the fundamental mathematical properties of the Fibonacci sequence.