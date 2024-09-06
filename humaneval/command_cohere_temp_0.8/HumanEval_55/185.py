```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n. It returns the nth Fibonacci number. The base cases are handled with the conditional statement `if n <= 1:`, where fib(0) returns 0 and fib(1) returns 1. For n greater than 1, the function recursively calls itself with the arguments n-1 and n-2, and adds the results to compute the Fibonacci number. This approach leverages the inherent nature of Fibonacci numbers, where each number is a sum of the two preceding ones.