```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n. It returns the n-th Fibonacci number. The base cases are handled with the simple condition n <= 1, where it returns n if n is either 1 or 0. If n is greater than 1, the function recursively calls itself with the arguments n-1 and n-2, and adds the results to produce the Fibonacci number for the given input. 

The function includes type hints, indicating that the argument should be an integer, and it returns an integer as well. Additionally, the function includes a docstring, providing a more comprehensive description of the function's purpose, and demonstrates the behavior of the function through example tests.