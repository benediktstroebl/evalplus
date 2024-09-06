```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python code defines a function called fib that calculates the n-th Fibonacci number. The base case checks if n is less than or equal to 1, in which case it returns n as the first two numbers in the Fibonacci sequence are 0 and 1. If n is greater than 1, the function recursively calls itself with the arguments n-1 and n-2, and returns the sum of the results of these recursive calls, which is how the Fibonacci sequence is defined.