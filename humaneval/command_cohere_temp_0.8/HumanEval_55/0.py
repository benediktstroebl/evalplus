```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a Python function called fib that takes an integer n as input. It employs a recursive approach to calculate the Fibonacci number for n. If n is less than or equal to 1, it returns n directly. Otherwise, it recursively calls itself twice with arguments n-1 and n-2, summing up the results to provide the Fibonacci number for n. This function encapsulates the entire Fibonacci sequence calculation and offers a convenient way to retrieve specific Fibonacci numbers.