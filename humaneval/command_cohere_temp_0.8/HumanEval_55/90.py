```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, taking a single argument n, which returns the nth Fibonacci number. The base case checks if n is less than 2, in which case it returns n, as the first two Fibonacci numbers are 0 and 1. Otherwise, it recursively calls fib(n-1) and fib(n-2) to calculate the sum of the two previous Fibonacci numbers, which is the desired nth Fibonacci number. This code correctly solves the problem of calculating the Fibonacci numbers and achieves the goal in a more efficient and readable manner compared to directly calculating large Fibonacci numbers.