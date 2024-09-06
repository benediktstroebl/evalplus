```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n. It returns the nth Fibonacci number. The base cases are handled with the condition `if n <= 1`, where it returns n if n is either 1 or 0, assuming the first two Fibonacci numbers are 0 and 1. For larger values of n, it recursively calls itself with the arguments n-1 and n-2, and adds the results to compute the Fibonacci number. This approach is efficient due to the cancellation of multiples of the two-term recurrence relation.