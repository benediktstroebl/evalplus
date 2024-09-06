```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n, which represents the index of the Fibonacci number to be returned. The function starts with a base case, checking if n is less than 2 (0 or 1). If so, it returns n, as the base Fibonacci numbers are 0 and 1. If n is greater than or equal to 2, the function recursively calls itself with the arguments n-1 and n-2, and returns the sum of the results of these recursive calls, which will be the Fibonacci number at position n. 

This recursive approach efficiently calculates Fibonacci numbers without the need for explicit recursion termination, providing a convenient way to access Fibonacci numbers in Python.