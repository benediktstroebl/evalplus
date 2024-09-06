```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. The function calculates and returns the nth Fibonacci number. It incorporates a base case to handle scenarios where n is less than or equal to 1, returning n directly in such cases. For larger values of n, the function recursively computes the Fibonacci number by summing the results of the (n-1)th and (n-2)th Fibonacci numbers, effectively achieving the Fibonacci sequence recurrence relation.