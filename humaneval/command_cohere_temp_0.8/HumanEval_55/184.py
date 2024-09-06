```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the nth Fibonacci number. The base cases are handled with the conditional statement `if n <= 1:`. If n is either 1 or 0, it returns n as the first two numbers in the Fibonacci sequence are 0 and 1. If n is greater than 1, the function recursively calls itself with the arguments n-1 and n-2, and returns the sum of the results of these two recursive calls. This is how the Fibonacci sequence is defined: each number is the sum of the two preceding ones. This script provides a concise and efficient way to calculate Fibonacci numbers.