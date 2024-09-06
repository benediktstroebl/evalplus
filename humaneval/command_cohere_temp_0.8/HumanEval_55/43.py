```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This function uses a recursive approach to calculate the Fibonacci sequence, which is an efficient solution for this problem. The base cases are defined with `if n < 2`, where `n` returns `n` when `n` is less than 2, and for `n` greater than or equal to 2, it returns the summation of the previous two numbers in the sequence.