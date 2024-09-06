```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python code defines a function called fib that calculates the n-th Fibonacci number. The base case checks if n is less than or equal to 1, in which case it returns n itself (since the first two Fibonacci numbers are 0 and 1). If n is greater than 1, the function recursively calls itself to calculate the sum of the (n-1)th and (n-2)th Fibonacci numbers, which is the definition of the Fibonacci sequence.