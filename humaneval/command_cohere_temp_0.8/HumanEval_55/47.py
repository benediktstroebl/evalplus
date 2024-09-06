```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer parameter n, which represents the index of the Fibonacci number to be returned. The function begins by checking if n is less than or equal to 1. If so, it returns n itself, as the base cases of the Fibonacci sequence are 0 and 1. If n is greater than 1, the function recursively calls itself with the arguments n-1 and n-2, and returns the sum of the results of these recursive calls, effectively calculating the nth Fibonacci number using the recurrence relation of the Fibonacci sequence.