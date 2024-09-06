```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the nth Fibonacci number. The base cases are handled with the conditional statement `if n <= 1:`, where it returns n if n is either 1 or 0, assuming the first two Fibonacci numbers are 0 and 1. If n is greater than 1, it recursively calls itself with the inputs n-1 and n-2, and returns the sum of the results of these recursive calls, which will be the (n+1)th Fibonacci number. This code assumes that the Fibonacci sequence starts with 0 and 1, which is a common convention. 
```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```
These assertions demonstrate that the function correctly calculates the 10th, 1st, and 8th Fibonacci numbers, respectively.