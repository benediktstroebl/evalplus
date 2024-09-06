```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. The function calculates and returns the n-th Fibonacci number. This is achieved through a recursive approach, where the function calls itself recursively with the arguments n-1 and n-2, representing the two previous Fibonacci numbers. The base cases are also incorporated with the if statement to handle n values less than or equal to 1, where the function directly returns n or 1, respectively, as these are the first two Fibonacci numbers.