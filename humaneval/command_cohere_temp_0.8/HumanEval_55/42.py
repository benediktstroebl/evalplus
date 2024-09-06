```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This function uses a recursive approach to calculate the Fibonacci sequence, which is an efficient solution for this problem. The function first checks if the input `n` is less than 2, returning `n` if true. If not, it returns the sum of the two previous numbers in the sequence, which achieves the correct solution and fulfills the given examples in the description.