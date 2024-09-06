```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single integer argument n, which represents the index of the Fibonacci number to be returned. The function starts with a base case, checking if n is less than 2 (0 or 1). If so, it returns n, as the base Fibonacci numbers are 0 and 1. If n is greater than or equal to 2, the function recursively calls itself with the arguments n-1 and n-2, and returns the sum of the results of these recursive calls, which is the essence of the Fibonacci sequence. 
The functiondocs explain the purpose and behavior of the function and include usage examples in the format expected in the Python documentation style, demonstrating the return of the 10th, 1st, and 8th Fibonacci numbers when the function is called with these indices.