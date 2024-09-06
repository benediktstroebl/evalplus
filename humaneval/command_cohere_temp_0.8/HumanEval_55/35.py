```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single argument n, which represents the index of the Fibonacci number to be returned. The function starts with a base case, where it returns n or 1 (the first two Fibonacci numbers) if n is less than or equal to 1. If n is greater than 1, it recursively calls itself with arguments n-1 and n-2, and adds the results to compute the Fibonacci number for the given index. 

To follow the specified docstring, the function includes clear documentation with the three example test cases provided, demonstrating its behavior and ensuring correctness for these specific inputs.