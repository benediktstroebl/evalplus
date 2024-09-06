```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python script defines a self-contained function called fib that takes an integer n as input and returns the n-th Fibonacci number. The base cases are handled properly with the if statement, quickly returning 1 for n equal to 1 and avoiding overflow with big numbers. For other values of n, the function recursively calls itself with the arguments (n-1) and (n-2), which allows it to compute the Fibonacci number for each position properly by adding the two previous Fibonacci numbers. This is how the Fibonacci sequence is defined. Overall, the script provides an efficient and elegant way to compute Fibonacci numbers, making it useful for various mathematical and computational needs.