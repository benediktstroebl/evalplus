```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python code defines a function called fib that calculates the n-th Fibonacci number. The base case checks if n is less than or equal to 1, in which case it returns n itself (since the first two Fibonacci numbers are 0 and 1). If n is greater than 1, the function recursively calls itself with the arguments n-1 and n-2, and returns the sum of the results of these recursive calls, which is the essence of the Fibonacci sequence.