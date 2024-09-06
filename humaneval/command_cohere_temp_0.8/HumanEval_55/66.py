```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the nth Fibonacci number. The base cases are handled with the conditional statement `if n <= 1`, where it returns n if n is either 1 or 0, which are the first two numbers in the Fibonacci sequence. If n is greater than 1, it recursively calls itself with the arguments n-1 and n-2, and adds the results to compute the next Fibonacci number. This script provides a straightforward implementation of the Fibonacci sequence without requiring any external libraries. 
```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```
These test cases validate the correctness of the fib function for various inputs.