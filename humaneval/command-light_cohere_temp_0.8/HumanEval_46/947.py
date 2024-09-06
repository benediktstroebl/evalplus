```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two previous numbers.

    :return fib4(0) == 0
    return (fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4))
```
The function calculates the nth Fibonacci number in a single pass and does not use recursion.