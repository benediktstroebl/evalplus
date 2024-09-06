```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python code defines a function called fib that takes an integer n as input. It employs a recursive approach to calculate the Fibonacci number for n. If n is less than or equal to 1, it returns n directly. Otherwise, it recursively calls itself with the inputs n-1 and n-2, and combines the results of these recursive calls to provide the Fibonacci number for the given input.