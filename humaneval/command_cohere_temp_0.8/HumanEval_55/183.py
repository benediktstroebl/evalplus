```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n. It returns the nth Fibonacci number. The base cases are handled with the conditional statement `if n <= 1`, where fib(0) returns 0 and fib(1) returns 1. For n > 1, the function recursively calls itself with arguments n-1 and n-2, and adds the results to compute the Fibonacci number for n. This approach leverages the recursive nature of Fibonacci sequencing, avoiding redundant calculations.