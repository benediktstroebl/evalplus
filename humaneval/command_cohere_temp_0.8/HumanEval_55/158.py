```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. The function calculates and returns the n-th Fibonacci number. This is achieved through a recursive approach, where the function calls itself recursively with the arguments n-1 and n-2, representing the two previous Fibonacci numbers. The base cases are also implemented with the lines:
```python
if n <= 1:
    return n
else:
    return fib(n-1) + fib(n-2)
```
These base cases handle situations where n is either 1 or less than 1, directly returning n as the first Fibonacci number (since the function is initialized with 0 and 1 in the first two calls). For any other value of n, the function recursively calculates the n-th Fibonacci number by summing the results of the previous two recursive calls.