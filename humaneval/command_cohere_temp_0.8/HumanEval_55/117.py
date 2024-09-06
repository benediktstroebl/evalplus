```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. The function calculates and returns the nth Fibonacci number. It incorporates a base case to handle n values less than or equal to 1, where it directly returns n. For larger n values, the function recursively calls itself with the arguments n-1 and n-2, summing up the results of these recursive calls to provide the Fibonacci number for the given input.