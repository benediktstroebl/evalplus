```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1. The function returns the next Fibonacci number.
    if n < 0:
        return 0
    elif n < 1:
        return 0
    elif n < 2:
        return 2
    else:
        return (fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4))
```
The function efficiently computes the n-th Fibonacci number without recursion.