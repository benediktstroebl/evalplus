```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which the next number is defined as the sum of the two preceding ones. Fibonacci numbers are general formula for computing the n-th Fibonacci number is given by: 
    f(n) = f(n-1) + f(n-2) 
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) 
```
The function above will return the n-th Fibonacci number, given an integer n as input.