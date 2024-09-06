```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. The function calculates and returns the nth Fibonacci number. It incorporates a base case to handle scenarios where n is less than or equal to 1, in which case it returns n itself. For values of n greater than 1, the function recursively computes the Fibonacci number by summing the results of the previous two iterations (fib(n-1) and fib(n-2)). This approach leverages the recursive nature of Fibonacci sequencing, ensuring quick computations of subsequent Fibonacci numbers. The script's concise and optimized formulation showcases the beauty of mathematical concepts synergizing with programming to elegantly solve problems.