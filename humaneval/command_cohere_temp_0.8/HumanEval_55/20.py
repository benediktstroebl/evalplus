```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. The function calculates and returns the nth Fibonacci number. It utilizes a recursive approach, where the function first handles base cases by returning n or 1 when n is less than or equal to 1. If n is greater than 1, it recursively calls itself with arguments n-1 and n-2, and adds the results to compute the Fibonacci number. This recursive approach mirrors the definition of Fibonacci numbers, where each number is the sum of the two preceding ones.