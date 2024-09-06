```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This function uses a recursive approach to calculate the Fibonacci sequence, which is an efficient way to compute the sequence for small or moderate values of `n`. It leverages the fact that each Fibonacci number can be expressed as the sum of the two preceding numbers in the sequence.