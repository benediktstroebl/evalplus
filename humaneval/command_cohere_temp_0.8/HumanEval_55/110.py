```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python script defines a self-contained function called fib that takes an integer n as input and returns the n-th Fibonacci number. The function utilizes a recursive approach to calculate Fibonacci numbers, where each invocation recursively calculates the sum of the two preceding numbers in the sequence. The base cases are handled with the function returning n (or 1 when n is 0) when n is equal to or less than 1. 

This approach, while elegant, can become inefficient for larger values of n due to the repeated recalculations of overlapping subproblems, resulting in an exponential time complexity. However, it beautifully demonstrates the essence of recursion and the Fibonacci sequence.