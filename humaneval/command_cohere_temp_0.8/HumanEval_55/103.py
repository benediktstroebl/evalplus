```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the nth Fibonacci number. The base cases are handled with the condition `if n <= 1:`, where it returns n if n is either 1 or 0, assuming these are the first two Fibonacci numbers. If n is greater than 1, it recursively calls itself with the arguments n-1 and n-2, and adds the results to compute the Fibonacci number for n. Overall, this function calculates the Fibonacci sequence by recursively adding the two previous numbers until it reaches the base case.