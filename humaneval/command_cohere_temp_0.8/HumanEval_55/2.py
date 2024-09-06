```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python code defines a function called fib that takes an integer n as input and returns the n-th Fibonacci number. The base case checks if n is less than 2, in which case it returns n, knowing that the first two numbers in the Fibonacci sequence are 0 and 1. If n is greater than or equal to 2, the function recursively calls itself with the arguments n-1 and n-2, and adds the results, thereby calculating the Fibonacci number for the given input. 

To use this code, you can call the fib function with a specific value of n to obtain the corresponding Fibonacci number. For example, calling fib(10) would return 55, fib(1) would return 1, and fib(8) would return 21.