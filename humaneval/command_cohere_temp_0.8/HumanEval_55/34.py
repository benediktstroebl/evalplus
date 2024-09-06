```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `Fibonacci sequence` is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. This python script provides a function called `fib`, which calculates the nth Fibonacci number. It works by recursively calling itself to calculate the previous two Fibonacci numbers and adding them together to solve for the next number in the sequence. It is optimized to handle the base cases of `n = 1` and `n = 2` directly, avoiding unnecessary calculations and displaying the appropriate values for these cases.