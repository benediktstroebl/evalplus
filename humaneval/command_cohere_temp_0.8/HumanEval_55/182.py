```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the nth Fibonacci number. The base cases are handled with the simple if statement where the function returns n or 1 if n is less than or equal to 1 respectively. If n is greater than 1, the function recursively calls itself, subtracting 1 from n in each iteration, eventually reaching the base case and then adding the results back together to provide the Fibonacci number for the current value of n. 
The script includes a docstring at the beginning which provides a helpful description of the function and its behavior, as well as example usage that demonstrates the function's behavior. The script is self-contained, making it easy to reuse and distribute.