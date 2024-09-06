```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. The function calculates and returns the n-th Fibonacci number. This is achieved through a recursive approach, where the function calls itself recursively with the arguments n-1 and n-2, representing the two preceding Fibonacci numbers. The base cases are also implemented with the Fibonacci of 0 and 1 both being 1. And the function returns n for these cases.