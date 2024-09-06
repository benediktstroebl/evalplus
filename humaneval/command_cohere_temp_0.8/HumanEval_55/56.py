```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. The function calculates and returns the n-th Fibonacci number. This is achieved through a recursive approach, where the function calls itself with two successive Fibonacci numbers and adds them together to obtain the next Fibonacci number.