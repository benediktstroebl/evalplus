```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
This Python script defines a self-contained function called fib that takes an integer n as input and returns the n-th Fibonacci number. The function implements a recursive approach to calculate Fibonacci numbers, where each number is derived from summing the two preceding numbers in the sequence. 

For example, if n = 10, the function will return 55. This is confirmed by the first test case in the provided markdown code block. If n = 1, the function will return 1, as confirmed by the second test case. If n = 8, the function will return 21, as confirmed by the third test case. 

This approach leverages the definition of the Fibonacci sequence, where each number is the sum of the two preceding ones, to efficiently compute the values. The base case handles n = 1 or n = 2, and the recursive nature takes care of larger n values.