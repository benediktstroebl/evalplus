```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n. It returns the nth Fibonacci number. The base cases are handled with the conditional statement `if n <= 1`, where it returns n if n is either 1 or 0, which are the first two numbers in the Fibonacci sequence. If n is greater than 1, it recursively calls itself with the arguments n-1 and n-2, and adds the results to compute the nth Fibonacci number. This code correctly implements the Fibonacci sequence without any external dependencies.